import argparse

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", type=str, default="test", help="run name")

    parser.add_argument("--task", type=str, help="Task: train/test")
    parser.add_argument("--device", type=str, default="cuda:0", help="cuda device to use")
    parser.add_argument("--arch", type=str, default="nodown", help="architecture name")
    parser.add_argument("--freeze", action='store_true', help="Freeze all layers except the last one")
    parser.add_argument("--prototype", action='store_true', help="Use prototypes")
    parser.add_argument("--num_centers",type=int, default=1, help="Number of prototypes centers")

    parser.add_argument("--num_epoches", type=int, default=100, help="# of epoches at starting learning rate")
    parser.add_argument("--lr", type=float, default=0.0001, help="initial learning rate")
    parser.add_argument("--lr_decay_epochs",type=int, default=5, help="Number of epochs without loss reduction before lowering the learning rate by 10x")
    parser.add_argument("--lr_min",type=float, default=1e-7, help="Number of epochs without loss reduction before lowering the learning rate by 10x")

    parser.add_argument("--split_file", type=str, help="Path to split json")
    parser.add_argument("--data_root", type=str, help="Path to dataset")
    parser.add_argument("--data_keys", type=str, help="Dataset specifications")

    parser.add_argument("--batch_size", type=int, default=64, help='Dataloader batch size')
    parser.add_argument("--num_threads", type=int, default=14, help='# threads for loading data') # 14 for locutus / 16 for hal
    
    return parser