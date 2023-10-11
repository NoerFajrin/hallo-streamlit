import streamlit as st
import requests
import matplotlib.pyplot as plt
import pandas as pd

# URL API
api_url = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota"

# Fungsi untuk mendapatkan data dari API
def get_api_data():
    response = requests.get(api_url)
    return response.json()

# Tampilkan data dalam bentuk grafik batang
st.title("Data Balita Stunting di Jawa Barat")

data = get_api_data()

# Periksa apakah respon API valid
if "data" in data:
    st.write("Data Balita Stunting:")

    # Buat DataFrame dari data
    df = pd.DataFrame(data["data"])

    # Daftar kabupaten/kota unik
    kabupaten_kota_list = df["nama_kabupaten_kota"].unique()

    # Buat satu grafik batang untuk setiap kabupaten/kota
    st.write("Grafik Jumlah Balita Stunting per Kabupaten/Kota berdasarkan Tahun")
    for kabupaten_kota in kabupaten_kota_list:
        data_kabupaten = df[df["nama_kabupaten_kota"] == kabupaten_kota]
        plt.figure(figsize=(12, 6))
        plt.bar(data_kabupaten["tahun"], data_kabupaten["jumlah_balita_stunting"])
        plt.xlabel('Tahun')
        plt.ylabel('Jumlah Balita Stunting')
        plt.title(f'Grafik Jumlah Balita Stunting di {kabupaten_kota}')
        st.write(f'Grafik untuk {kabupaten_kota}')
        st.pyplot(plt)

else:
    st.write("Tidak ada data yang tersedia.")
