from PIL import Image
import numpy as np
import tensorflow as tf

# Load and preprocess the image
image = Image.open('number.png').convert("L")  # Convert to grayscale
resized_image = image.resize((28, 28))  # Resize to (28, 28)
np_image = np.array(resized_image)  # Convert to numpy array
np_image = np_image / 255.0  # Normalize pixel values to range [0, 1]
np_image = np_image.reshape(1, 28, 28, 1)  # Reshape to (1, 28, 28, 1) as the model expects

model = tf.keras.models.load_model('mnist_predictor.h5')

predictions = model.predict(np_image)
print(f"The model predicts {np.array(predictions).argmax()}!")
print(predictions)
