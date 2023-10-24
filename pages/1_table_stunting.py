import streamlit as st
import requests

# URL API
api_url = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota"

# Fungsi untuk mendapatkan data dari API
def get_api_data():
    response = requests.get(api_url)
    return response.json()

# Tampilkan data dalam bentuk tabel
st.title("Data Balita Stunting di Jawa Barat")

data = get_api_data()

# Periksa apakah respon API valid
if "data" in data:
    st.write("Data Balita Stunting:")

    # Buat daftar untuk tabel
    table_data = []
    for item in data["data"]:
        row = {
            "Kabupaten/Kota": item['nama_kabupaten_kota'],
            "Jumlah Balita Stunting": item['jumlah_balita_stunting'],
            "Tahun": item['tahun'] if item['tahun'] != "Unknown Type: integer)" else "Tahun tidak valid"
        }
        table_data.append(row)

    # Tampilkan data dalam tabel
    st.table(table_data)
else:
    st.write("Tidak ada data yang tersedia.")
