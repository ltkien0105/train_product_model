import os
import shutil
fruits = len(os.listdir('dataset/val/Fruit'))
packages = len(os.listdir('dataset/val/Packages'))
vegetables = len(os.listdir('dataset/val/Vegetables'))

print(fruits + packages + vegetables)
# fruits = os.listdir('dataset/val/Packages')
# for fruit in fruits:
#     # if ((not os.path.exists(f'dataset/val/Packages/{fruit}'))
#     #     or (not os.path.exists(f'dataset/train/Packages/{fruit}'))
#     # ):
#     #     continue
#     if ((os.path.exists(f'dataset/train/Packages/{fruit}_val'))):
#         continue
#     fr_val = os.listdir(f'dataset/val/Packages/{fruit}')

#     fr_train = os.listdir(f'dataset/train/Packages/{fruit}')
#     num_fr_val = len(fr_val)
#     num_fr_train = len(fr_train)
#     sum_fr = num_fr_val + num_fr_train
#     val_rest = int(sum_fr/5)
#     val_rest = num_fr_val - val_rest
#     os.makedirs(f'dataset/train/Packages/{fruit}_val')
#     for i in range(val_rest):
#         shutil.move(
#             f'dataset/val/Packages/{fruit}/{fr_val[i]}',
#             f'dataset/train/Packages/{fruit}_val', 
#         )