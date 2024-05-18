# Streamlit Documentation: https://docs.streamlit.io/

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 
from textwrap import fill
import pickle
import requests
import json
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder

st.sidebar.markdown("# Main page 🎈")

import streamlit as st

import streamlit as st

css = '''
    <style>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
'''

st.markdown(css, unsafe_allow_html=True)

st.markdown('<div class="container">'
            '<h1>Diamond Price Prediction App</h1>'
            '</div>',
            unsafe_allow_html=True)


# Add image
img = Image.open("D3.jpg")
st.image(img, caption="Diamond")



import streamlit as st

css = '''
    <style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .text {
        
        font-size: 24px;
    }
    </style>
'''

st.markdown(css, unsafe_allow_html=True)

st.markdown('<div class="container">'
            '<p class="text">Welcome to the Diamond Price Prediction App! Diamonds are one of the most precious gemstones, and their prices can vary based on various factors such as carat weight, color, clarity, and more.</p>'
            '<p class="text">This app utilizes the power of Data Science and Machine Learning to help you predict the price of a diamond based on its characteristics. Whether you are a diamond enthusiast, a jeweler, or simply curious about diamond prices, this app is designed to provide valuable insights and predictions.</p>'
            '<p class="text">By inputting the relevant attributes of a diamond, such as carat weight, color, clarity, and more, the app will leverage a trained machine learning model to estimate the price of the diamond. You can explore different scenarios and observe how each attribute impacts the predicted price.</p>'
            '<p class="text">Let\'s embark on this diamond price prediction journey and unlock the power of data-driven insights!</p>'
            '<p class="text">*Note: The predictions provided by this app are based on a trained model and should be used for informational purposes only.*</p>'
            '</div>',
            unsafe_allow_html=True)









# st.header("About")
# st.markdown('')
# st.markdown("")

