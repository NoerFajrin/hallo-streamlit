import streamlit as st
import requests

# URL API
api_url = "https://data.jabarprov.go.id/api-backend//bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota?limit=300"

# Fungsi untuk mendapatkan data dari API
def get_api_data():
    response = requests.get(api_url)
    return response.json()

# Tampilkan data asli dalam format JSON
st.title("Data Balita Stunting di Jawa Barat")

data = get_api_data()

# Periksa apakah respon API valid
if "data" in data:
    st.write("Data Balita Stunting:")
    st.json(data["data"])
else:
    st.write("Tidak ada data yang tersedia.")
