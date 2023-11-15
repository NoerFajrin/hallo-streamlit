import streamlit as st
from PIL import Image


st.title("Sistem Desain")
image = Image.open("/aset/desain.png")
st.image(image)
