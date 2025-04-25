import os
import torch
from torchvision import datasets
import torchvision.transforms.v2 as Tv2

from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import json
import bisect

def parse_dataset(settings):
    gen_keys = {
        'gan1':['StyleGAN'],
        'gan2':['StyleGAN2'],
        'gan3':['StyleGAN3'],
        'sd15':['StableDiffusion1.5'],
        'sd2':['StableDiffusion2'],
        'sd3':['StableDiffusion3'],
        'sdXL':['StableDiffusionXL'],
        'flux':['FLUX.1'],
        'realFFHQ':['FFHQ'],
        'realFORLAB':['FORLAB']
    }

    gen_keys['all'] =   [gen_keys[key][0] for key in gen_keys.keys()]
    # gen_keys['gan'] =   [gen_keys[key][0] for key in gen_keys.keys() if 'gan'   in key]
    # gen_keys['sd'] =    [gen_keys[key][0] for key in gen_keys.keys() if 'sd'    in key]
    gen_keys['real'] =  [gen_keys[key][0] for key in gen_keys.keys() if 'real'  in key]

    mod_keys = {
        'pre':  ['PreSocial'],
        'fb':   ['Facebook'],
        'tl':   ['Telegram'],
        'tw':   ['Twitter'],
    }

    mod_keys['all'] = [mod_keys[key][0] for key in mod_keys.keys()]
    mod_keys['shr'] = [mod_keys[key][0] for key in mod_keys.keys() if key in ['fb', 'tl', 'tw']]

    need_real = (settings.task == 'train' and not len([data.split(':')[0] for data in settings.data_keys.split('&') if 'real' in data.split(':')[0]]))

    assert not need_real, 'Train task without real data, this will not get handeled automatically, terminating'

    dataset_list = []
    for data in settings.data_keys.split('&'):
        gen, mod = data.split(':')
        dataset_list.append({'gen':gen_keys[gen], 'mod':mod_keys[mod]})
    
    return dataset_list

class TrueFake_dataset(datasets.DatasetFolder):
    def __init__(self, settings):
        self.data_root = settings.data_root
        self.split = settings.split

        with open(settings.split_file, "r") as f:
            split_list = sorted(json.load(f)[self.split])
        
        dataset_list = parse_dataset(settings)
        
        self.samples = []
        self.info = []
        for dict in dataset_list:
            generators = dict['gen']
            modifiers = dict['mod']

            for mod in modifiers:
                for dataset_root, dataset_dirs, dataset_files in os.walk(os.path.join(self.data_root, mod), topdown=True, followlinks=True):
                    if len(dataset_dirs):
                        continue

                    (label, gen, sub)  = f'{dataset_root}/'.replace(os.path.join(self.data_root, mod) + os.sep, '').split(os.sep)[:3]
                    
                    if gen in generators:
                        for filename in sorted(dataset_files):
                            if os.path.splitext(filename)[1].lower() in ['.png', '.jpg', '.jpeg']:
                                if self._in_list(split_list, os.path.join(gen, sub, os.path.splitext(filename)[0])):
                                    self.samples.append(os.path.join(dataset_root, filename))
                                    self.info.append((mod, label, gen, sub))

        self.transform_start = Tv2.Compose(
            [
                Tv2.ToImage()
            ]
        )

        self.transform_end = Tv2.Compose(
            [
                Tv2.CenterCrop(1024)    if self.split == 'test' and 'realFORLAB:pre'    in settings.data_keys  else Tv2.Identity(),
                Tv2.CenterCrop(720)     if self.split == 'test' and 'realFORLAB:fb'     in settings.data_keys  else Tv2.Identity(),
                Tv2.CenterCrop(1200)    if self.split == 'test' and 'realFORLAB:tw'     in settings.data_keys  else Tv2.Identity(),
                Tv2.CenterCrop(800)     if self.split == 'test' and 'realFORLAB:tl'     in settings.data_keys  else Tv2.Identity(),
                Tv2.ToDtype(torch.float32, scale=True),
                Tv2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ]
        )

        if self.split in ['train', 'val']:
            self.transform_aug = {
                'light': Tv2.Compose(
                                        [
                                            Tv2.RandomChoice([Tv2.RandomResizedCrop([300], (0.5, 1.5), (0.5, 2)), Tv2.RandomCrop([300])], p=[0.3, 0.7]),
                                            Tv2.Compose([Tv2.RandomHorizontalFlip(p=0.5), Tv2.RandomVerticalFlip(p=0.5)]),
                                            Tv2.RandomCrop(96, pad_if_needed=True) if self.split == 'train' else Tv2.Identity(),
                                        ]
                                    ),
                'heavy': Tv2.Compose(
                                        [
                                            Tv2.RandomChoice([Tv2.RandomResizedCrop([300], (0.5, 1.5), (0.5, 2)), Tv2.RandomCrop([300])], p=[0.3, 0.7]),

                                            Tv2.RandomApply([Tv2.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.4, hue=0.1)], p=0.3),
                                            Tv2.RandomApply([Tv2.GaussianBlur(kernel_size=11, sigma=(0.1,3))], p=0.3),
                                            Tv2.RandomApply([Tv2.JPEG((65, 95))], p=0.3),

                                            Tv2.Compose([Tv2.RandomHorizontalFlip(p=0.5), Tv2.RandomVerticalFlip(p=0.5)]),

                                            Tv2.RandomCrop(96, pad_if_needed=True) if self.split == 'train' else Tv2.Identity(),
                                        ]
                                    )
            }

        else:
            self.transform_aug = None
        
        print()
        print(f'Transforms for {self.split}:')
        print(self.transform_start)
        if self.transform_aug:
            print(self.transform_aug['light'])
            print(self.transform_aug['heavy'])
        print(self.transform_end)

        print(f'Loaded {len(self.samples)} samples for {self.split}')
                    
    def _in_list(self, split, elem):
        i = bisect.bisect_left(split, elem)
        return i != len(split) and split[i] == elem
    
    def __len__(self):
        return len(self.samples)
    
    def __getitem__(self, index):
        path = self.samples[index]
        mod, label, gen, sub = self.info[index]

        image = Image.open(path).convert('RGB')
        sample = self.transform_start(image)
        if self.transform_aug:
            sample = self.transform_aug['heavy' if mod == 'PreSocial' else 'light'](sample)
        sample = self.transform_end(sample)

        target = 1.0 if label == 'Fake' else 0.0
        
        return sample, target, path

def create_dataloader(settings, split=None):
    if split == "train":
        settings.split = 'train'
        is_train=True

    elif split == "val":
        settings.split = 'val'
        is_train=False
    
    elif split == "test":
        settings.split = 'test'
        settings.batch_size = settings.batch_size//8
        is_train=False
    
    else:
        raise ValueError(f"Unknown split {split}")

    dataset = TrueFake_dataset(settings)

    data_loader = torch.utils.data.DataLoader(
        dataset,
        batch_size=settings.batch_size,
        num_workers=int(settings.num_threads),
        shuffle = is_train,
        collate_fn=None,
    )
    return data_loader
