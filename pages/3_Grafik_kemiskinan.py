import streamlit as st
import requests
import plotly.express as px
import pandas as pd

# URL API
api_url = "https://data.jabarprov.go.id/api-backend/bigdata/bps/od_20000_indeks_kedalaman_kemiskinan_berdasarkan_kabupatenkota?limit=1000&where=%7B%22tahun%22%3A%5B%222014%22%2C%222015%22%2C%222016%22%2C%222017%22%2C%222018%22%2C%222019%22%2C%222020%22%2C%222021%22%2C%222022%22%5D%7D"

# Fungsi untuk mendapatkan data dari API
def get_api_data():
    response = requests.get(api_url)
    return response.json()

# Tampilkan data dalam bentuk tabel
st.title("Grafik Indeks Kemiskinan Berdasarkan Kabupaten/Kota di Jawa Barat")

data = get_api_data()

# Periksa apakah respon API valid
if "data" in data:
    st.write("Berikut ini adalah Grafik Indeks Kemiskinan:")

    # Buat daftar unik tahun dari data dan urutkan
    years = sorted(list(set(item['tahun'] for item in data["data"])))

    # Pilih tahun menggunakan widget
    selected_year = st.selectbox("Pilih Tahun:", years)

    # Buat daftar untuk grafik berdasarkan tahun yang dipilih
    graph_data = []
    for item in data["data"]:
        if item['tahun'] == selected_year:
            row = {
                "Kabupaten/Kota": item['nama_kabupaten_kota'],
                "Indeks Kemiskinan": item['indeks_kedalaman_kemiskinan'],
            }
            graph_data.append(row)

    # Konversi data ke DataFrame
    df = pd.DataFrame(graph_data)

    # Membuat grafik menggunakan plotly
    fig = px.bar(df, x='Kabupaten/Kota', y='Indeks Kemiskinan', title=f'Indeks Kemiskinan di Jawa Barat ({selected_year})')
    st.plotly_chart(fig)
else:
    st.write("Tidak ada data yang tersedia.")
