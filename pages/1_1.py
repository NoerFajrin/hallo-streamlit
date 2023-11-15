import streamlit as st
from PIL import Image


st.title("haha")
image = Image.open("/aset/desain.png")
st.image(image)
