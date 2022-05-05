import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.text_input("Your name", key="name")
st.session_state.name


st.header("Generate ASCII images using GAN")
st.write("Choose any image and get corresponding ASCII art:")

uploaded_file = st.file_uploader("Choose an image...")

if uploaded_file is not None:
    # src_image = load_image(uploaded_file)
    image = Image.open(uploaded_file)

    st.image(uploaded_file, caption='Input Image', use_column_width=True)


