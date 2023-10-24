import streamlit as st
import requests

# URL API
api_url = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota?limit=300"

# Fungsi untuk mendapatkan data dari API
def get_api_data():
    response = requests.get(api_url)
    return response.json()

# Tampilkan data dalam bentuk tabel
st.title("Tabel Data Balita Stunting di Jawa Barat")

data = get_api_data()

# Periksa apakah respon API valid
if "data" in data:
    st.write("Data Balita Stunting:")

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
                "Jumlah Balita Stunting": item['jumlah_balita_stunting'],
                "Tahun": item['tahun']
            }
            table_data.append(row)

    # Tampilkan data dalam tabel
    st.table(table_data)
else:
    st.write("Tidak ada data yang tersedia.")
