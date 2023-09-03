import tensorflow as tf
from tensorflow import keras
import cv2, os
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # '0' (default) '1' (errors) '2' (warnings and erros) '3' (no output)

# Initialize an empty NumPy array for training data
training_data = []
Camila_Cabello_covers=[] 
other_covers=[]
labels = []
for f in os.listdir("D:\camila_image"):
    Camila_Cabello_covers.append(os.path.join("D:\camila_image",f))
for f in os.listdir("D:\images"):
    other_covers.append(os.path.join("D:\images",f))

for cover_path in Camila_Cabello_covers:
    img = cv2.imread(cover_path)
    img = cv2.resize(img, (64, 64))
    training_data.append(img)
    labels.append(1)  # 1 represents Camila Cabello album cover


for other_path in other_covers:
    img = cv2.imread(other_path)
    img = cv2.resize(img, (64, 64))
    training_data.append(img)
    labels.append(0)  # 0 represents other images

# Convert lists to NumPy arrays
training_data = np.array(training_data)
labels = np.array(labels)
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model with dataset
model.fit(training_data, labels, epochs=10, verbose=0)

def predict_album_cover(image_path):
    # Load and preprocess the image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (64, 64))
    img = img / 255.0  # Normalize pixel values
    # Make predictions
    prediction = model.predict(np.array([img]), verbose=0)
    if prediction[0] > 0.5:
        return "Camila Cabello Album Cover"
    else:
        return "Not a Camila Cabello Album Cover"
