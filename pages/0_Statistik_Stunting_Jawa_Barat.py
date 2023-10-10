import streamlit as st
import requests

# URL API
url = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota"

# Mengambil data dari API
response = requests.get(url)

if response.status_code == 200:
    data_stunting = response.json()
else:
    st.error("Gagal mengambil data dari API")

# Judul Aplikasi
st.title("Data Stunting di Jawa Barat")

# Tampilkan Data Stunting
if 'data_stunting' in locals():
    st.write("Data Stunting terbaru di Jawa Barat:")
    st.write(data_stunting)