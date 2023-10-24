import streamlit as st
import requests

# URL API
api_url = "https://data.jabarprov.go.id/api-backend/bigdata/bps/od_20000_indeks_kedalaman_kemiskinan_berdasarkan_kabupatenkota?limit=1000&where={%22tahun%22:[%222014%22,%222015%22,%222016%22,%222017%22,%222018%22]}"

# Fungsi untuk mendapatkan data dari API
def get_api_data():
    response = requests.get(api_url)
    return response.json()

# Tampilkan data dalam bentuk tabel
st.title("Tabel Indeks Kemiskinan Berdasarkan Kabupaten/Kota di Jawa Barat (2014-2018)")

data = get_api_data()

# Periksa apakah respon API valid
if "data" in data:
    st.write("Berikut ini adalah Tabel Indeks Kemiskinan:")

    # Buat daftar unik tahun dari data dan urutkan
    years = sorted(list(set(item['tahun'] for item in data["data"])))

    # Pilih tahun menggunakan widget
    selected_year = st.selectbox("Pilih Tahun:", years)

    # Buat daftar untuk tabel berdasarkan tahun yang dipilih
    table_data = []
    for item in data["data"]:
        if item['tahun'] == selected_year:
            row = {
                "Kabupaten/Kota": item['nama_kabupaten_kota'],
                "Indeks Kemiskinan": item['indeks_kedalaman_kemiskinan'],
                "Tahun": item['tahun']
            }
            table_data.append(row)

    # Tampilkan data dalam tabel
    st.table(table_data)
else:
    st.write("Tidak ada data yang tersedia.")
