import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

train_dir = 'dataset/train'
val_dir = 'dataset/val'
test_dir = 'dataset/test'

train_dataset = image_dataset_from_directory(
    train_dir,
    image_size=(256, 256),
    batch_size=32
)

val_dataset = image_dataset_from_directory(
    val_dir,
    image_size=(256, 256),
    batch_size=32
)

test_dataset = image_dataset_from_directory(
    train_dir,
    image_size=(256, 256),
    batch_size=32
)

class_names = train_dataset.class_names

# plt.figure(figsize=(10, 10))
# for images, labels in train_dataset.take(1):
#     for i in range(9):
#         ax = plt.subplot(3, 3, i + 1)
#         plt.imshow(images[i].numpy().astype("uint8"))
#         plt.title(class_names[labels[i]])
#         plt.axis("off")
# plt.show()

model = models.Sequential([
    layers.Rescaling(1./255, input_shape=(256, 256, 3)),  # Normalize the data
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(len(class_names), activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=10
)

test_loss, test_acc = model.evaluate(test_dataset)
print(f'Test accuracy: {test_acc:.2f}')

model.save('my_model.h5')
