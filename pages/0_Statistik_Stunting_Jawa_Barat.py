import streamlit
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
st.write(data)  # Tampilkan data JSON

