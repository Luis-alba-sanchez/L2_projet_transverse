import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# st.text_input("Your name", key="name")
# st.session_state.name

st.set_page_config(page_title='MyColon', page_icon='img/Colon_onglet.png')

st.header("Generate ASCII images using GAN")
st.subheader("Writer and Developer")
st.write("Choose any image and get corresponding ASCII art:")

uploaded_file = st.file_uploader("Select JPG file :",
                                 ['jpg'],
                                 help="Drag and drop the jpg file here")

if uploaded_file is not None:
    # src_image = load_image(uploaded_file)
    image = Image.open(uploaded_file)

    st.image(uploaded_file, caption='Input Image', use_column_width=True)

st.markdown('Streamlit is **_really_ cool**.', unsafe_allow_html=True)