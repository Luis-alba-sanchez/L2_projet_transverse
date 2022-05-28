import streamlit as st
from PIL import Image

# ---- Onglet ----
st.set_page_config(page_title='MyColon', page_icon='img/Colon_onglet.png')


# ---- Title ----
with st.container():
    col1, col2 = st.columns([1, 3])
    with col1:
        image_title = Image.open('img/Colon3.png')
        st.image(image_title)
    with col2:
        st.header("Do you want to know your patient colon situation ?")
    st.write("*This website allow you to know if your patient have a colon inflammation*")


# ---- image downloading ----
with st.container():
    st.write("##")
    st.write("---")
    st.write("##")
    uploaded_file = st.file_uploader("Select JPG file :",
                                     ['jpg'],
                                     help="Drag and drop the jpg file here")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(uploaded_file, caption='Image saved', use_column_width=True)


# ---- A propos ----
with st.container():
    st.write("##")
    st.write("---")
    st.write("##")
    with st.expander("A propos"):
        st.write("""
             bla bla bla.
         """)
