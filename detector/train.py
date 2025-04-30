# ----------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------
import os
os.environ['CUDA_LAUNCH_BLOCKING'] = '1'
import glob
import torch
import shutil
from tqdm import tqdm
import torch.nn as nn
import torch.optim as optim

from networks import ImageClassifier
from parser import get_parser
from dataset import create_dataloader
from sklearn.metrics import balanced_accuracy_score

def check_accuracy(val_dataloader, model, settings):
    model.eval()
    
    label_array = torch.empty(0, dtype=torch.int64, device=device)
    pred_array = torch.empty(0, dtype=torch.int64, device=device)

    with torch.no_grad():
        with tqdm(val_dataloader, unit='batch', mininterval=0.5) as tbatch:
            tbatch.set_description(f'Validation')
            for (data, label, _) in tbatch:
                data = data.to(device)
                label = label.to(device)
                
                pred = model(data).squeeze(1)
                
                label_array = torch.cat((label_array, label))
                pred_array = torch.cat((pred_array, pred))
    
    accuracy = balanced_accuracy_score(label_array.cpu().numpy(), pred_array.cpu().numpy() > 0)

    print(f'Got accuracy {accuracy:.2f} \n')
    return accuracy


def train(train_dataloader, val_dataloader, model, settings):
    best_accuracy = 0
    lr_decay_counter = 0
    for epoch in range(0, settings.num_epoches):
        model.train()
        with tqdm(train_dataloader, unit='batch', mininterval=0.5) as tepoch:
            tepoch.set_description(f'Epoch {epoch}', refresh=False)
            for batch_idx, (data, label, _) in enumerate(tepoch):
                data = data.to(device)
                label = label.to(device).float()

                scores = model(data).squeeze(1)

                loss = criterion(scores, label).mean()

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                
                tepoch.set_postfix(loss=loss.item())

        if epoch % 20 == 0:
            torch.save(model.state_dict(), f'./train/{settings.name}/models/epoch_{epoch}.pt')

        accuracy = check_accuracy(val_dataloader, model, settings)

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            torch.save(model.state_dict(), f'./train/{settings.name}/models/best.pt')

            print(f'New best model saved with accuracy {best_accuracy:.4f} \n')
            lr_decay_counter = 0

        elif settings.lr_decay_epochs > 0:
            lr_decay_counter += 1
            if lr_decay_counter == settings.lr_decay_epochs:
                if optimizer.param_groups[0]['lr'] > settings.lr_min:
                    for param_group in optimizer.param_groups:
                        param_group['lr'] *= 0.1
                    print('Learning rate decayed \n')
                    lr_decay_counter = 0
                else:
                    print('Learning rate already at minimum \n')
                    break

if __name__ == "__main__":
    parser = get_parser()
    settings = parser.parse_args()
    print(settings)

    device = torch.device(settings.device if torch.cuda.is_available() else 'cpu')

    model = ImageClassifier(settings)
    model.to(device)
    
    os.makedirs(f'./train/{settings.name}/models', exist_ok=True)
    for file in glob.glob(f'*.py'):
        shutil.copy(file, f'./train/{settings.name}/')
    
    with open(f'./train/{settings.name}/settings.txt', 'w') as f:
        f.write(str(settings))

    train_dataloader = create_dataloader(settings, split='train')
    val_dataloader = create_dataloader(settings, split='val')

    optimizer = optim.Adam((p for p in model.parameters() if p.requires_grad), lr=settings.lr)

    criterion = nn.BCEWithLogitsLoss(reduction='none')

    train(train_dataloader, val_dataloader, model, settings)