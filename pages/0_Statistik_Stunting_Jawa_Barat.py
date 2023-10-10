import streamlit as st
import requests

# URL API
api_url = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota"

# Fungsi untuk mendapatkan data dari API
def get_api_data():
    response = requests.get(api_url)
    return response.json()

# Tampilkan data di Streamlit
st.title("Data Balita Stunting di Jawa Barat")

data = get_api_data()

# Periksa apakah respon API valid
if "data" in data:
    st.write("Data Balita Stunting:")
    for item in data["data"]:
        st.write(f"Kabupaten/Kota: {item['nama_kabupaten_kota']}")
        st.write(f"Jumlah Balita Stunting: {item['jumlah_balita_stunting']}")
        if item['tahun'] != "Unknown Type: integer)":
            st.write(f"Tahun: {item['tahun']}")
        st.write("")

else:
    st.write("Tidak ada data yang tersedia.")

