import numpy as np
import pickle
import streamlit as st
from PIL import Image
from predict_processor import process
from tensorflow import keras


model = keras.models.load_model('cnn_main.keras')


uploaded_file = st.file_uploader("Choose a file", type=['jpg', 'jpeg', 'png'], accept_multiple_files=False)

if uploaded_file is not None:
    st.image(uploaded_file)
    if(st.button("Check for mask")):
        img = process(uploaded_file)
        ans = model.predict(img)
        if ans>=0.5:
            st.markdown("Wearing a mask")
        else:
            st.markdown("Not Wearing a mask")

img=st.camera_input("OR TAKE PHOTO (in lighting with a smile.)")
if (img is not None):
    if(st.button("Check for mask")):
        img = process(img)
        ans = model.predict(img)
        if ans>=0.5:
            st.markdown("Wearing a mask")
        else:
            st.markdown("Not Wearing a mask")

