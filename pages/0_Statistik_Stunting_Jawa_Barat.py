import streamlit as st
import requests

# URL API
url = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota"

# Mengambil data dari API
try:
    response = requests.get(url)

    if response.status_code == 200:
        data_stunting = response.json()
    else:
        st.error(f"API request failed with status code {response.status_code}")
except Exception as e:
    st.error(f"An error occurred while fetching data from the API: {str(e)}")

# Rest of your Streamlit code
