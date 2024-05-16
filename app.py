import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np
from PIL import Image

# Custom CSS for better styling
st.markdown("""
    <style>
        .main-header {
            font-size:36px;
            color:#ff6347;
            font-weight: bold;
            text-align: center;
        }
        .sub-header {
            font-size:24px;
            color:#4682b4;
            text-align: center;
            margin-bottom:20px;
        }
        .prediction-text {
            font-size:24px;
            color:#32cd32;
            font-weight: bold;
            text-align: center;
        }
        .accuracy-text {
            font-size:20px;
            color:#ff4500;
            font-weight: bold;
            text-align: center;
        }
        .upload-box {
            display: flex;
            justify-content: center;
        }
        .uploaded-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">Image Classification Model</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Upload an image of a fruit or vegetable and the model will classify it for you!</p>', unsafe_allow_html=True)

# Load the model
model_path = 'models\\fruitmodel.h5'
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

# File uploader for image
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file is not None:
    try:
        # Display a progress bar while processing
        with st.spinner('Processing...'):
            # Load and preprocess the image
            image = Image.open(uploaded_file)
            image = image.resize((img_height, img_width))
            img_arr = tf.keras.preprocessing.image.img_to_array(image)
            img_bat = np.expand_dims(img_arr, axis=0)

            # Predict the class
            predict = model.predict(img_bat)
            score = tf.nn.softmax(predict[0])

        # Display the image and prediction results
        st.image(image, caption='Uploaded Image', use_column_width=False, width=150, output_format='auto', channels='RGB')
        st.markdown(f'<p class="prediction-text">Veg/Fruit in image is: {data_cat[np.argmax(score)]}</p>', unsafe_allow_html=True)

        st.success('Thank you for using the Image Classification Model!')

    except Exception as e:
        st.error("Error processing the image. Please try again.")
        st.write(str(e))
else:
    st.info("Please upload an image file to get a prediction.")
