import streamlit as st
from PIL import Image


st.title("Desain Sistem")
image = Image.open("/aset/desain.png")
st.image(image)
