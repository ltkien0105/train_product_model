from transformers import CLIPProcessor, CLIPModel
from create_insert_each_folder import get_img_path_list

import os
dict_categories = {
    'Beverages': 1,
    'Condiments & Sauces': 2,
    'Dairy & Alternatives': 3,
    'Fruits': 4,
    'Proteins': 5,
    'Snacks & Sweets': 6,
    'Staples & Grains': 7,
    'Vegetables': 8,
    'Coffee': 9,
    'Juice': 10,
    'Soda': 11,
    'Tea': 12,
    'Water': 13,
    'Honey': 14,
    'Jam': 15,
    'Spices': 16,
    'Tomato_sauce': 17,
    'Vinegar': 18,
    'Milk': 19,
    'Oat-milk': 20,
    'Oatghurt': 21,
    'Sour-cream': 22,
    'Sour-milk': 23,
    'Soy-milk': 24,
    'Soyghurt': 25,
    'Yoghurt': 26,
    'Apple': 27,
    'Avocado': 28,
    'Banana': 29,
    'Kiwi': 30,
    'Lemon': 31,
    'Lime': 32,
    'Mango': 33,
    'Melon': 34,
    'Nectarine': 35,
    'Orange': 36,
    'Papaya': 37,
    'Passion-fruit': 38,
    'Peach': 39,
    'Pear': 40,
    'Pineapple': 41,
    'Plum': 42,
    'Pomegranate': 43,
    'Red-grapefruit': 44,
    'Satsumas': 45,
    'Fish': 46,
    'Nuts': 47,
    'Cake': 48,
    'Candy': 49,
    'Chips': 50,
    'Chocolate': 51,
    'Beans': 52,
    'Cereal': 53,
    'Flour': 54,
    'Oil': 55,
    'Pasta': 56,
    'Rice': 57,
    'Sugar': 58,
    'Asparagus': 59,
    'Aubergine': 60,
    'Brown-cap-mushroom': 61,
    'Cabbage': 62,
    'Carrots': 63,
    'Corn': 64,
    'Cucumber': 65,
    'Garlic': 66,
    'Ginger': 67,
    'Leek': 68,
    'Mushroom': 69,
    'Onion': 70,
    'Pepper': 71,
    'Potato': 72,
    'Red-beet': 73,
    'Tomato': 74,
    'Zucchini': 75,
}

processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
def compute_image_embeddings(list_of_images):
    return model.get_image_features(**processor(images=list_of_images, return_tensors="pt", padding=True))

category = 'Beverages'
types = ['JUICE', 'SODA']
print(types)
for type in types:
    print(type.capitalize())
    category_id = dict_categories[type.capitalize()]
    with open(f'sql/{category}_{type.capitalize()}.txt', 'w') as insert_file:
        imgs = get_img_path_list(category, type)
        image_features = compute_image_embeddings(imgs)
        for embedding in image_features.detach().numpy():
            embedding_list = embedding.tolist()
            insert_file.write(f'INSERT INTO images(category_id, embedding) VALUES({category_id}, \'{embedding_list}\');\n')
        print(f'{category} -> {type.capitalize()}: {len(image_features.detach().numpy())}')
        insert_file.close()