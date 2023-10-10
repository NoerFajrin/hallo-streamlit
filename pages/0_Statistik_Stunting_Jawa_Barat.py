import streamlit as st
import requests
import pandas as pd

# URL API
url = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota"

# Mengambil data dari API
response = requests.get(url)

if response.status_code == 200:
    api_data = response.json()
else:
    st.error("Gagal mengambil data dari API")

# Judul Aplikasi
st.title("Data Stunting di Jawa Barat")

# Tampilkan Data Stunting dalam bentuk tabel jika data tersedia
if 'api_data' in locals():
    st.write("Data Stunting terbaru di Jawa Barat:")
    
    if 'data' in api_data:
        data = api_data['data']
        
        # Membuat DataFrame dengan baris yang sesuai dengan bidang data
        df = pd.DataFrame.from_records([data])
        
        # Tampilkan DataFrame sebagai tabel di Streamlit
        st.table(df)
    else:
        st.warning("Data tidak tersedia.")
