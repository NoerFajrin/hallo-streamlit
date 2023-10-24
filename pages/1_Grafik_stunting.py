import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# URL API
api_url = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota?limit=300"

# Fungsi untuk mendapatkan data dari API
def get_api_data():
    response = requests.get(api_url)
    return response.json()

# Tampilkan data dalam bentuk grafik
st.title("Grafik Data Balita Stunting di Jawa Barat")

data = get_api_data()

# Periksa apakah respon API valid
if "data" in data:
    st.write("Grafik Jumlah Balita Stunting di Provinsi Jawa Barat")

    # Buat DataFrame dari data
    df = pd.DataFrame(data["data"])

    # Buat daftar unik tahun dari data
    years = sorted(df["tahun"].unique())

    # Pilih tahun menggunakan widget
    selected_year = st.selectbox("Pilih Tahun:", years)

    # Filter data berdasarkan tahun yang dipilih
    filtered_data = df[df["tahun"] == selected_year]

    # Buat grafik batang
    fig = px.bar(
        filtered_data,
        x="nama_kabupaten_kota",
        y="jumlah_balita_stunting",
        title=f"Jumlah Balita Stunting di Jawa Barat Tahun {selected_year}",
        labels={"jumlah_balita_stunting": "Jumlah Balita Stunting", "nama_kabupaten_kota": "Kabupaten/Kota"}
    )

    # Tampilkan grafik
    st.plotly_chart(fig)
else:
    st.write("Tidak ada data yang tersedia.")
