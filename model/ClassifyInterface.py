MODEL_RELATIVE_PATH = 'trained-20241210-064520.keras'

import os
import numpy as np

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = ""
import tensorflow as tf
from tensorflow import keras
tf.config.set_visible_devices([], 'GPU')
print("Using CPU only.")

class ClassifyInterface:
    def __init__(self):
        self.__model_path = os.path.join(os.path.dirname(__file__), MODEL_RELATIVE_PATH)
        print(self.__model_path)
        self.model = tf.keras.models.load_model(self.__model_path)
        self.reverse_label_dict = {
            '一般 general': 0, 
            '塑膠 plastic': 1, 
            '廚餘 food_waste': 2, 
            '廢紙 waste_paper': 3, 
            '玻璃 glass': 4, 
            '衣服類 clothes (Textiles)': 5, 
            '鐵鋁金屬 iron alumium': 6, 
            '電池類 battery': 7
        }
        self.label_dict = {value: key for key, value in self.reverse_label_dict.items()}
        print("[Initalized]")

    def predict(self, img_path: str):
        print(f"Predicting: {img_path}")
        if not os.path.isfile(img_path):
            return {'label': -1, 'label_name': 'ERROR'}
        else:
            base_image_path = keras.utils.load_img(os.path.abspath(img_path))
            img = keras.preprocessing.image.load_img(img_path, target_size=(128, 128))
            # Convert the image to a numpy array
            img_array = keras.preprocessing.image.img_to_array(img)
            # Expand dimensions to match the input shape of the model (batch size, height, width, channels)
            img_array = np.expand_dims(img_array, axis=0)

            # Optionally normalize the image (if required by your model)
            img_array = img_array / 255.0  # Rescale to [0, 1] if necessary
            prediction = self.model.predict(img_array)
            Y_pred = int(np.argmax(prediction))
            result = {'label': Y_pred, 'label_name': self.label_dict[Y_pred]}
            print(result)
            return result

    def predict_multiple(self, img_paths: list):
        # List to store processed images
        img_batch = []

        # Preprocess all images
        for img_path in img_paths:
            img = keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
            img_array = keras.preprocessing.image.img_to_array(img)
            img_array = img_array/255.0  # Preprocess input for ResNet50
            img_batch.append(img_array)

        # Stack all images into a single numpy array (batch dimension)
        img_batch = np.array(img_batch)

        # Make batch predictions
        predictions = self.model.predict(img_batch)

        

