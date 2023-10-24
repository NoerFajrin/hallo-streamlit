import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# URL API for the first dataset
api_url_stunting = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota?limit=300"

# URL API for the second dataset
api_url_poverty = "https://data.jabarprov.go.id/api-backend/bigdata/bps/od_20000_indeks_kedalaman_kemiskinan_berdasarkan_kabupatenkota?limit=1000&where=%7B%22tahun%22%3A%5B%222014%22%2C%222015%22%2C%222016%22%2C%222017%22%2C%222018%22%2C%222019%22%2C%222020%22%2C%222021%22%2C%222022%22%5D%7D"

# Fungsi untuk mendapatkan data dari API
def get_api_data(api_url):
    response = requests.get(api_url)
    return response.json()

# Tampilkan data dalam bentuk grafik
st.title("Data Visualizations in Jawa Barat")

# Fetch data from the first API
data_stunting = get_api_data(api_url_stunting)

# Periksa apakah respon API valid
if "data" in data_stunting:
    st.write("Grafik Jumlah Balita Stunting di Provinsi Jawa Barat")

    # Buat DataFrame dari data
    df_stunting = pd.DataFrame(data_stunting["data"])

    # Buat daftar unik tahun dari data
    years_stunting = sorted(df_stunting["tahun"].unique())

    # Pilih tahun menggunakan widget
    selected_year_stunting = st.selectbox("Pilih Tahun untuk Balita Stunting:", years_stunting)

    # Filter data berdasarkan tahun yang dipilih
    filtered_data_stunting = df_stunting[df_stunting["tahun"] == selected_year_stunting]

    # Buat grafik batang
    fig_stunting = px.bar(
        filtered_data_stunting,
        x="nama_kabupaten_kota",
        y="jumlah_balita_stunting",
        title=f"Jumlah Balita Stunting di Jawa Barat Tahun {selected_year_stunting}",
        labels={"jumlah_balita_stunting": "Jumlah Balita Stunting", "nama_kabupaten_kota": "Kabupaten/Kota"}
    )

    # Tampilkan grafik
    st.plotly_chart(fig_stunting)
else:
    st.write("Tidak ada data yang tersedia untuk Balita Stunting.")

# Fetch data from the second API
data_poverty = get_api_data(api_url_poverty)

# Periksa apakah respon API valid
if "data" in data_poverty:
    st.write("Grafik Indeks Kemiskinan di Jawa Barat")

    # Buat DataFrame dari data
    df_poverty = pd.DataFrame(data_poverty["data"])

    # Buat daftar unik tahun dari data dan urutkan
    years_poverty = sorted(list(set(item['tahun'] for item in data_poverty["data"]))

    # Pilih tahun menggunakan widget
    selected_year_poverty = st.selectbox("Pilih Tahun untuk Indeks Kemiskinan:", years_poverty)

    # Buat daftar untuk grafik berdasarkan tahun yang dipilih
    graph_data_poverty = []
    for item in data_poverty["data"]:
        if item['tahun'] == selected_year_poverty:
            row = {
                "Kabupaten/Kota": item['nama_kabupaten_kota'],
                "Indeks Kemiskinan": item['indeks_kedalaman_kemiskinan'],
            }
            graph_data_poverty.append(row)

    # Konversi data ke DataFrame
    df_poverty_selected = pd.DataFrame(graph_data_poverty)

    # Membuat grafik menggunakan plotly
    fig_poverty = px.bar(df_poverty_selected, x='Kabupaten/Kota', y='Indeks Kemiskinan', title=f'Indeks Kemiskinan di Jawa Barat ({selected_year_poverty})')
    st.plotly_chart(fig_poverty)
else:
    st.write("Tidak ada data yang tersedia untuk Indeks Kemiskinan.")
