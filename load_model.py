from tensorflow import keras
from tensorflow.keras.preprocessing import image_dataset_from_directory
import numpy as np

model = keras.models.load_model("model/my_model.keras")

test_dir = 'dataset/test'
val_dir = 'dataset/val'

test_dataset = image_dataset_from_directory(
    test_dir,
    image_size=(256, 256),
    batch_size=32
)
val_dataset = image_dataset_from_directory(
    val_dir,
    image_size=(256, 256),
    batch_size=32
)
dataset = val_dataset

predictions = model.predict(dataset)
predicted_classes = np.argmax(predictions, axis=1)  # Find the index of the max probability

test_images, test_labels = zip(*[(images, labels) for images, labels in dataset])
test_labels = np.concatenate(test_labels)

# Calculate accuracy by comparing predicted classes and true labels
accuracy = np.mean(predicted_classes == test_labels)
print(f"Test accuracy: {accuracy * 100:.2f}%")

# Print the predicted class labels
print("Predicted classes:", predicted_classes)