import streamlit as st
import requests
import pandas as pd

# URL API
url = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota"

# Mengambil data dari API
response = requests.get(url)

if response.status_code == 200:
    api_data = response.json()
    data_stunting = api_data['data']
else:
    st.error("Gagal mengambil data dari API")

# Judul Aplikasi
st.title("Data Stunting di Jawa Barat")

# Tampilkan Data Stunting dalam Tabel
if 'data_stunting' in locals():
    # Buat DataFrame dari data stunting
    df = pd.DataFrame(data_stunting, index=[0])

    # Tampilkan DataFrame sebagai tabel
    st.write("Data Stunting terbaru di Jawa Barat:")
    st.dataframe(df)

# Munculkan kesalahan jika gagal mengambil data
if 'data_stunting' not in locals():
    st.error("Gagal mengambil data dari API")
