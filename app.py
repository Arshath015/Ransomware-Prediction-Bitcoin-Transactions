import numpy as np
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model.pkl')  # Replace with your model file path

# Background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        bg_img = file.read()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bg_img}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Replace 'background.jpg' with the path to your image file
add_bg_from_local('background.jpg')

# Streamlit app title
st.title("Ransomware Attack Detection in Bitcoin Transactions")

# Collect user input
year = st.number_input('Year')
day = st.number_input('Day')
length = st.number_input('Length')
weight = st.number_input('Weight')
count = st.number_input('Count')
looped = st.number_input('Looped')
neighbors = st.number_input('Neighbors')
income = st.number_input('Income')

# Prediction button
if st.button('Predict'):
    # Prepare the input data
    input_data = pd.DataFrame({
        'year': [year],
        'day': [day],
        'length': [length],
        'weight': [weight],
        'count': [count],
        'looped': [looped],
        'neighbors': [neighbors],
        'income': [income]
    })

    st.write("Input Data:", input_data)  # Debugging: Check the input data

    # Make prediction
    prediction = model.predict(input_data)
    
    st.write("Prediction Raw Output:", prediction)  # Debugging: Check the prediction value
    
    # Ensure prediction is a single integer
    if isinstance(prediction, np.ndarray):
        prediction = prediction[0]

    # Define mapping of prediction to labels
    label_mapping = {
        0: 'montrealCryptXXX',
        1: 'montrealCryptoLocker',
        2: 'paduaCryptoWall',
        3: 'princetonCerber',
        4: 'princetonLocky',
        5: 'white'
    }

    # Check if the prediction is valid
    if prediction in label_mapping:
        st.success(f'Predicted Ransomware Attack Type: {label_mapping[prediction]}')
    else:
        st.error("Prediction returned a Someother Ransomeware attack")
