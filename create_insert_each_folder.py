from PIL import Image
import os

def get_img_path_list(category, type):
    img_name_list = os.listdir(f'dataset_merge/{category}/{type}')
    img_path_list = [f'dataset_merge/{category}/{type}/{img_name}' for img_name in img_name_list]
    imgs = [Image.open(img_path) for img_path in img_path_list]

    return imgs

