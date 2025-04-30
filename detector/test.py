# ----------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------
import os
import torch
from tqdm import tqdm

from networks import ImageClassifier
from parser import get_parser
from dataset import create_dataloader

def test(loader, model, settings):
    model.eval()

    csv_filename = f'./train/{settings.name}/data/{settings.data_keys}/results.csv'

    with open(csv_filename, 'w') as f:
        f.write(f"{','.join(['name', 'pro', 'flag'])}\n")
    
    with torch.no_grad():
        with tqdm(loader, unit='batch', mininterval=0.5) as tbatch:
            tbatch.set_description(f'Validation')
            for (data, labels, paths) in tbatch:
                data = data.to(device)
                labels = labels.to(device)

                scores = model(data).squeeze(1)

                with open(csv_filename, 'a') as f:
                    for score, label, path in zip(scores, labels, paths):
                        f.write(f"{path}, {score.item()}, {label.item()}\n")

if __name__ == "__main__":
    parser = get_parser()
    settings = parser.parse_args()
    
    device = torch.device(settings.device if torch.cuda.is_available() else 'cpu')

    os.makedirs(f'./train/{settings.name}/data/{settings.data_keys}', exist_ok=True)
    test_dataloader = create_dataloader(settings, split='test')

    model = ImageClassifier(settings)
    model.to(device)

    state_dict = torch.load(f'./train/{settings.name}/models/best.pt')
    model.load_state_dict(state_dict)

    test(test_dataloader, model, settings)