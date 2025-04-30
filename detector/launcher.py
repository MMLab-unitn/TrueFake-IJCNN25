
import os
import subprocess 
import time

def autotest(train_list, data_list):
    assert type(data_list) == list
    task_list = []
    for train in train_list:
        task_list.append({'type':'train', 'details':train})
        for data in data_list:
            name = train['data']
            task_list.append({'type':'test', 'details':{'detector': train['detector'], 'model': name, 'data': data}})

    return task_list

dataset_path = os.path.join(os.sep, 'media', 'mmlab', 'Datasets_4TB', 'TrueFake')
device_override = 'cuda:1'

split_file = os.path.abspath('split.json')

os.makedirs('logs', exist_ok=True)

# only list the training/testing to perform
only_list = False
dry_run = False

# specify the phases to run {train, test}
phases = ['train', 'test']

device_override = 'cuda:0'

tasks = []

train = [
        {'detector': 'R50_ND', 'model': None, 'data': 'gan2:pre&sdXL:pre&realFFHQ:pre&realFORLAB:pre'},
        ]

test_list = [
            'realFFHQ:fb',  'realFORLAB:fb',  'gan1:fb',  'gan2:fb',  'gan3:fb',  'sd15:fb',  'sd2:fb',   'sd3:fb',   'sdXL:fb',  'flux:fb',
            'realFFHQ:tl',  'realFORLAB:tl',  'gan1:tl',  'gan2:tl',  'gan3:tl',  'sd15:tl',  'sd2:tl',   'sd3:tl',   'sdXL:tl',  'flux:tl',
            'realFFHQ:tw',  'realFORLAB:tw',  'gan1:tw',  'gan2:tw',  'gan3:tw',  'sd15:tw',  'sd2:tw',   'sd3:tw',   'sdXL:tw',  'flux:tw',
            'realFFHQ:pre', 'realFORLAB:pre', 'gan1:pre', 'gan2:pre', 'gan3:pre', 'sd15:pre', 'sd2:pre',  'sd3:pre',  'sdXL:pre', 'flux:pre',
            ]

tasks.extend(autotest(train, test_list))

print('Number of tasks:', len(tasks))
for task in tasks:
    print(task)

if only_list:
    quit()

# from here the launcher will create all the arguments to use when calling the train script
for task in tasks:
    if task['type'] not in phases:
        continue

    args = []
    if task['type'] == 'train':
        args.append(f'--name "{task["details"]["data"]}"')
    else:
        args.append(f'--name "{task["details"]["model"]}"')

    args.append(f'--split_file {split_file}')
    args.append(f'--task {task["type"]}')
    args.append(f'--num_threads {8}')
    args.append(f'--data_keys "{task["details"]["data"]}"')
    args.append(f'--data_root {dataset_path}')
    args.append(f'--device {device_override}')
    args.append(f'--arch nodown')
    args.append(f'--prototype')
    args.append(f'--freeze')

    args = ' '.join(args) 

    # call to train.py
    if not dry_run:
        log_file = f'logs/{task["type"]}_{task["details"]["detector"]}_{task["details"]["model"]}_{task["details"]["data"]}.log'
        with open(log_file, 'w') as f:
            cwd = os.getcwd()
            # os.chdir(f'./detectors/{task["details"]["detector"]}')

            start_time = time.time()

            runner = f'{task["type"]}.py'   
            print(f'Call to {runner} with: {args}')
            subprocess.run(f'python -u {runner} {args}', shell=True, stdout=f, stderr=f)

            end_time = time.time()
            print(f'Execution time: {end_time-start_time:.2f} seconds')

            print('#'*80)
            print('#'*80)

            # os.chdir(cwd)



