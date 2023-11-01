import streamlit as st
import pandas as pd
import pydeck as pdk
import requests

# Endpoint untuk data kota/kabupaten di Provinsi Jawa Barat
endpoint = 'https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten'

# Mengambil data dari endpoint
response = requests.get(endpoint)
st.write("Response Status Code:", response.status_code)
data = response.json().get('data', [])
st.write(data)
