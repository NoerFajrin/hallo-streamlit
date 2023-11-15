import streamlit as st
from PIL import Image

st.title("Sistem Desain")
image1 = Image.open("aset/desain.png")
st.image(image1)

st.title("Desain Hardware")
image2 = Image.open("aset/desainhw.png")
st.image(image2)
