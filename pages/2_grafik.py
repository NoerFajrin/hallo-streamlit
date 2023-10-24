import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# URL API untuk data Balita Stunting
api_url_stunting = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota?limit=300"

# URL API untuk data Indeks Kemiskinan
api_url_kemiskinan = "https://data.jabarprov.go.id/api-backend/bigdata/bps/od_20000_indeks_kedalaman_kemiskinan_berdasarkan_kabupatenkota?limit=1000&where=%7B%22tahun%22%3A%5B%222014%22%2C%222015%22%2C%222016%22%2C%222017%22%2C%222018%22%2C%222019%22%2C%222020%22%2C%222021%22%2C%222022%22%5D%7D"

# Fungsi untuk mendapatkan data dari API
def get_api_data(api_url):
    response = requests.get(api_url)
    return response.json()

# Tampilkan data dalam bentuk grafik
st.title("Data di Jawa Barat")

# Pilihan tahun untuk kedua data
years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
selected_year = st.selectbox("Pilih Tahun:", years)

# Data Balita Stunting
st.subheader("Data Balita Stunting")

data_stunting = get_api_data(api_url_stunting)

# Periksa apakah respon API valid
if "data" in data_stunting:
    st.write("Grafik Jumlah Balita Stunting di Provinsi Jawa Barat")

    # Buat DataFrame dari data
    df_stunting = pd.DataFrame(data_stunting["data"])

    # Filter data berdasarkan tahun yang dipilih
    filtered_data_stunting = df_stunting[df_stunting["tahun"] == selected_year]

    # Buat grafik batang untuk Balita Stunting
    fig_stunting = px.bar(
        filtered_data_stunting,
        x="nama_kabupaten_kota",
        y="jumlah_balita_stunting",
        title=f"Jumlah Balita Stunting di Jawa Barat Tahun {selected_year}",
        labels={"jumlah_balita_stunting": "Jumlah Balita Stunting", "nama_kabupaten_kota": "Kabupaten/Kota"}
    )

    # Tampilkan grafik Balita Stunting di kolom kiri
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_stunting)

# Data Indeks Kemiskinan
col1, col2 = st.columns(2)
with col2:
    st.subheader("Data Indeks Kemiskinan")

    data_kemiskinan = get_api_data(api_url_kemiskinan)

    # Periksa apakah respon API valid
    if "data" in data_kemiskinan:
        st.write("Grafik Indeks Kemiskinan:")

        # Buat daftar untuk grafik berdasarkan tahun yang dipilih
        graph_data_kemiskinan = []
        for item in data_kemiskinan["data"]:
            if item['tahun'] == selected_year:
                row = {
                    "Kabupaten/Kota": item['nama_kabupaten_kota'],
                    "Indeks Kemiskinan": item['indeks_kedalaman_kemiskinan'],
                }
                graph_data_kemiskinan.append(row)

        # Konversi data ke DataFrame
        df_kemiskinan = pd.DataFrame(graph_data_kemiskinan)

        # Membuat grafik Indeks Kemiskinan menggunakan plotly
        fig_kemiskinan = px.bar(df_kemiskinan, x='Kabupaten/Kota', y='Indeks Kemiskinan', title=f'Indeks Kemiskinan di Jawa Barat ({selected_year})')
        st.plotly_chart(fig_kemiskinan)
    else:
        st.write("Tidak ada data Indeks Kemiskinan yang tersedia.")
