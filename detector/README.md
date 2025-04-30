# Data ID format
Data and models are defined by IDs specified using the following pattern: ```$(subset):$(share)```.

## Dataset format
The directory structure follows:
```
Dataset_root
├── Share#1
│   ├── Fake
│   │   ├── Subset#1
│   │   │   ├── Subsubset#1
│   │   │   └── Subsubset#2
│   │   ├── Subset#2
│   │   └── Subset#3
│   └── Real
│       ├── Dataset#1
│       └── Dataset#2
├── Share#2
│   ├── Fake
│   │   ├── Subset#1
│   │   │   ├── Subsubset#1
│   │   │   └── Subsubset#2
│   │   └── Subset#2
│   └── Real
│       ├── Subset#1
│       └── Subset#2
└── Share#3
    ├── Fake
    └── Real
```

## Data IDs
IDs are used as a compact way to specify which subset of data and share to use for the training and testing phases.
The list of possible subsets can be found [here](##subsets) and the list of possible shares key can be found [here](##shares)

For example: 
* ```gan:fb``` indicates all images generated using GAN methods and shared on facebook
* ```sd2:pre``` indicates images generated using StableDiffusion 2.1 that were not shared

### subsets
Available pairs of (key, subset) are:
```
'gan1':['StyleGAN']
'gan2':['StyleGAN2']
'gan3':['StyleGAN3']
'sd15':['StableDiffusion1.5']
'sd2':['StableDiffusion2']
'sd3':['StableDiffusion3']
'sdXL':['StableDiffusionXL']
'flux':['FLUX.1']
'realFFHQ':['FFHQ']
'realRAISE':['RAISE']
```

On top of these base ones the dataloader automatically add some useful ones:
```
'all': union of all sub-datasets
'gan': union of all sub-datasets that contain 'gan' in the key
'sd': union of all sub-datasets that contain 'sd' in the key
'real': union of all sub-datasets that contain 'real' in the key
```

IMPORTANT: the dataset walk is checked against the specified sub-datasets, if the sub-dataset does not exist the dataloader will not throw an error.

### shares
Available pairs of (key, share) are:
```
'pre': ['PreSocial']
'fb': ['Facebook']
'tl': ['Telegram']
'tw': ['Twitter']
```

Like for the sub-datasets the dataloader automatically add some useful pairs:
```
'all': union of all modifiers
'shr': union of modifiers with keys in ['fb', 'tl', 'tw']
```

## Combining IDs
IDs can be combined together using ```&```.\
```gan2:fb&sd3:pre``` indicates the union of images generated using StyleGAN2 and shared on facebook and images generated using StableDiffusion 3 that were not shared.

## Model IDs
A trained model has the same ID as the data that was used to train it:
* A clean model (ID = None) which is trained on ```sd2:pre``` will be identified by ```sd2:pre```
* For simplicity, a model originally trained on ```gan:fb``` and finetuned on ```sd:fb``` will be identified with ```sd:fb```