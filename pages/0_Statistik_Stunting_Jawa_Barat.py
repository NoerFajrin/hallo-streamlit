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
        
        # Ekstrak data ke dalam variabel yang sesuai
        id = data['id']
        jumlah_balita_stunting = data['jumlah_balita_stunting']
        kode_kabupaten_kota = data['kode_kabupaten_kota']
        kode_provinsi = data['kode_provinsi']
        nama_kabupaten_kota = data['nama_kabupaten_kota']
        nama_provinsi = data['nama_provinsi']
        satuan = data['satuan']
        tahun = data['tahun']

        # Buat DataFrame
        df = pd.DataFrame({
            'ID': [id],
            'Jumlah Balita Stunting': [jumlah_balita_stunting],
            'Kode Kabupaten/Kota': [kode_kabupaten_kota],
            'Kode Provinsi': [kode_provinsi],
            'Nama Kabupaten/Kota': [nama_kabupaten_kota],
            'Nama Provinsi': [nama_provinsi],
            'Satuan': [satuan],
            'Tahun': [tahun]
        })

        # Tampilkan DataFrame sebagai tabel di Streamlit
        st.table(df)
    else:
        st.warning("Data tidak tersedia.")
