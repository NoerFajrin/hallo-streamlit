import streamlit as st
import pandas as pd
import pydeck as pdk
import requests

# Define the API endpoints
endpoint_data_stunting = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota?limit=300"
endpoint_data_lat_lon = 'https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten'

# Make GET requests to the APIs
response = requests.get(endpoint_data_lat_lon)
responseStunting = requests.get(endpoint_data_stunting)

# Parse the JSON responses
data_lat_lon = response.json().get('data', [])
data_stunting = responseStunting.json().get('data', [])

# Create a list of years for selection
years = sorted(list(set(stunting_data["tahun"]
               for stunting_data in data_stunting)))

# Allow the user to select a year
selected_year = st.selectbox("Pilih Tahun:", years)

# Combine the data for the selected year
combined_data = []

for stunting_data in data_stunting:
    nama_kabupaten_kota_stunting = stunting_data["nama_kabupaten_kota"]
    jumlah_balita_stunting = stunting_data["jumlah_balita_stunting"]
    tahun = stunting_data["tahun"]

    # Filter data for the selected year
    if tahun == selected_year:
        # Find matching data in data_lat_lon based on the name of the kabupaten/kota
        matching_lat_lon_data = [
            item for item in data_lat_lon if item["bps_kota_nama"] == nama_kabupaten_kota_stunting]

        if matching_lat_lon_data:
            lat = matching_lat_lon_data[0]["latitude"]
            lon = matching_lat_lon_data[0]["longitude"]

            # Create a new data object
            data_baru = {
                "nama_kab": nama_kabupaten_kota_stunting,
                "lat": lat,
                "lon": lon,
                "balita_stunting": jumlah_balita_stunting,
                "tahun": tahun
            }

            combined_data.append(data_baru)

# Create a DataFrame
df = pd.DataFrame(combined_data)

# Konversi kolom "tahun" ke tipe data integer
unique_years = df['tahun'].unique()
st.write(unique_years)
# Display the combined data
st.write(df)
