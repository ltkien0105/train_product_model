from PIL import Image, UnidentifiedImageError
import os

medicine_train_folder = 'dataset/Medicine_train'
medicines = os.listdir(medicine_train_folder)
list_fail = []
for medicine in medicines:
    try:
        im = Image.open(medicine_train_folder + '/' + medicine)
        print(im.size)
    except UnidentifiedImageError:
        list_fail.append(medicine)

print(list_fail)