# Streamlit Documentation: https://docs.streamlit.io/

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 
from textwrap import fill
import pickle
import requests
import base64
import json
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder



# Content
css = '''
    <style>
    body {
        background-color: #000;
    }

    @keyframes shine {
        0% { color: #2980b9; text-shadow: 0 0 10px #2980b9; }
        50% { color: #000; text-shadow: 0 0 20px #000; }
        100% { color: #2980b9; text-shadow: 0 0 10px #2980b9; }
    }

    .center {
        text-align: center;
        margin: auto;
        font-family: Arial, sans-serif;
        font-size: 54px;
        animation: shine 25s infinite;
    }
    </style>
'''

st.markdown(css, unsafe_allow_html=True)
st.markdown('<h1 class="center">Diamond Price Prediction</h1>', unsafe_allow_html=True)



st.sidebar.markdown("# Prediction page 🎉")




# Define the CSS style
css = """
<style>
    .rounded-image {
        border-radius: 25px 10px ;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 50px;
        width: 91%;
        margin-left: 30px;
    }
</style>
"""

# Display the CSS style
st.markdown(css, unsafe_allow_html=True)

# Display the image with rounded corners
# image_path = 'D.png'
# image_html = f'<div class="rounded-image"><img src="data:image/jpeg;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}"></div>'
# st.markdown(image_html, unsafe_allow_html=True)
import base64

image_path = 'D.png'
image_html = f'''
    <div class="rounded-image">
        <img src="data:image/jpeg;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}"
        style="animation: updown 5s infinite;">
    </div>
'''

css = '''
    <style>
    @keyframes updown {
        0% { transform: translateY(0%); }
        50% { transform: translateY(-10%); }
        100% { transform: translateY(0%); }
    }
    </style>
'''

st.markdown(css + image_html, unsafe_allow_html=True)


# carat=st.sidebar.slider("Write a value for carat", 0.0,6.0, step=0.001)
# color=st.sidebar.selectbox("Choose a color:", ('D', 'E', 'F', 'G', 'H', 'I', 'J'))
# clarity=st.sidebar.selectbox("Choose a clarity:",('IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'))
# width=st.sidebar.slider("Select a width:", 1.0, 10.0, step=0.1)
carat = st.slider("Write a value for carat", 0.0, 6.0, step=0.001)
color = st.selectbox("Choose a color:", ('D', 'E', 'F', 'G', 'H', 'I', 'J'))
clarity = st.selectbox("Choose a clarity:", ('IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'))
width = st.slider("Select a width:", 1.0, 10.0, step=0.1)

filename = "final_rf"
model=pickle.load(open(filename, "rb"))


my_dict = {
    "carat": carat,
    "color": color,
    "clarity": clarity,
    "width": width
}


df = pd.DataFrame.from_dict([my_dict])

st.header("The values you have chosen: ")
st.table(df)



# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)
try:
    if predict:
        st.balloons()
        rounded_price = round(result[0], 3)
        st.success(f'The predicted price is: {rounded_price}$')
    else:
        st.warning('Choose values first')
except:
    st.warning('Something went wrong, please try again.')