import streamlit as st
import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

    # Membersihkan data dengan menghilangkan nilai "tahun" yang tidak valid
    df = df[df["tahun"] != "Unknown Type: integer)"]

    # Konversi kolom "tahun" menjadi tipe data integer
    df["tahun"] = df["tahun"].astype(int)

    # Ambil daftar tahun unik
    tahun_unik = df["tahun"].unique()

    # Pilih palet warna
    colors = plt.cm.viridis(np.linspace(0, 1, len(tahun_unik)))

    # Buat satu grafik batang untuk seluruh kabupaten/kota dalam satu chart
    plt.figure(figsize=(12, 6))
    for i, tahun in enumerate(tahun_unik):
        data_tahun = df[df["tahun"] == tahun]
        plt.bar(data_tahun["nama_kabupaten_kota"], data_tahun["jumlah_balita_stunting"], label=tahun, color=colors[i])

    plt.xlabel('Kabupaten/Kota')
    plt.ylabel('Jumlah Balita Stunting')
    plt.title('Grafik Jumlah Balita Stunting di Seluruh Kabupaten/Kota Berdasarkan Tahun')
    plt.legend(title='Tahun')
    plt.xticks(rotation=90)
    st.pyplot(plt)

else:
    st.write("Tidak ada data yang tersedia.")
