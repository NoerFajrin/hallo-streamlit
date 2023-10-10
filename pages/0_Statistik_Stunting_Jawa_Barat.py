import streamlit as st
import requests
import pandas as pd

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

# Tampilkan Data Stunting dalam bentuk tabel jika data tersedia
if 'data_stunting' in locals():
    st.write("Data Stunting terbaru di Jawa Barat:")
    
    # Ubah data ke dalam DataFrame Pandas
    if data_stunting and 'data' in data_stunting:
        df = pd.DataFrame(data_stunting['data'])
        
        # Tampilkan DataFrame sebagai tabel di Streamlit
        st.table(df)
    else:
        st.warning("Data tidak tersedia.")
