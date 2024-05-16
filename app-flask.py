import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from flask import Flask, request, jsonify, render_template
from PIL import Image
import io

app = Flask(__name__)

# Load the model
model_path = 'models/fruitmodel.h5'
model = load_model(model_path)

# Define the categories
data_cat = [
    'apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot', 
    'cauliflower', 'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger', 
    'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce', 'mango', 'onion', 'orange', 
    'paprika', 'pear', 'peas', 'pineapple', 'pomegranate', 'potato', 'raddish', 
    'soy beans', 'spinach', 'sweetcorn', 'sweetpotato', 'tomato', 'turnip', 'watermelon'
]

# Set image dimensions
img_height = 180
img_width = 180

def preprocess_image(image):
    image = image.resize((img_height, img_width))
    img_arr = tf.keras.preprocessing.image.img_to_array(image)
    img_bat = np.expand_dims(img_arr, axis=0)
    return img_bat

@app.route('/')
def home():
    return render_template('predict.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get the image file from the request
            file = request.files['file']
            # Read the image file
            image = Image.open(io.BytesIO(file.read()))
            # Preprocess the image
            processed_image = preprocess_image(image)
            # Predict the class
            prediction = model.predict(processed_image)
            # Get the predicted category
            predicted_category = data_cat[np.argmax(prediction)]
            return jsonify({'prediction': predicted_category})
        except Exception as e:
            return jsonify({'error': str(e)})
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
