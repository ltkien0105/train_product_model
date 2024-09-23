import os
lists = os.listdir('dataset/dataset/mfg')
lists.sort(key=lambda x: int(x.split('.')[0].split('_')[1]))
with open('dataset/dataset/label_mfg.txt', 'w') as label_exp:
    for item in lists:
        label_exp.write(item + '\t\n')