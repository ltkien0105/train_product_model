import os
lists = os.listdir('dataset/dataset/date')
lists.sort(key=lambda x: int(x.split('.')[0].split('_')[1]))
label_exp = []
with open('dataset/dataset/label_date.txt', 'r', encoding='utf-8') as label_exp_read:
    label_exp = label_exp_read.readlines()
    label_exp = [label.strip() for label in label_exp]
print(lists[:10])
print(label_exp[:10])

with open('dataset/dataset/label_date.txt', 'w', encoding='utf-8') as label_exp_write:
    for index, label in enumerate(label_exp):
        label_val = label.split('\t')[1]
        file_name = lists[index]
        label_exp_write.write(file_name + '\t' + label_val + '\n')