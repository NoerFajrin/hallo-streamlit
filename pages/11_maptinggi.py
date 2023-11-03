import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import requests

# Generate random data with elevation values
chart_data = pd.DataFrame({
    'lat': np.random.uniform(37.75, 37.77, 3),  # Adjust latitude range
    'lon': np.random.uniform(-122.45, -122.42, 3),  # Adjust longitude range
    'elevation': np.random.randint(0, 1000, 3)  # Elevation values
})

st.write(chart_data)
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

# Filter DataFrame for the selected year
filtered_data = df[df['tahun'] == selected_year]
# Convert the 'tahun' and 'balita_stunting' columns to strings
filtered_data['tahun'] = filtered_data['tahun'].astype(str)
filtered_data['balita_stunting'] = filtered_data['balita_stunting'].astype(int)
min_stunting = filtered_data['balita_stunting'].min().astype(int)
max_stunting = filtered_data['balita_stunting'].max().astype(int)
st.write(min_stunting)
st.write(max_stunting)
st.write(filtered_data)

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=filtered_data['lat'].mean(),
        longitude=filtered_data['lon'].mean(),
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=filtered_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
            auto_highlight=True,
            pickable=True,
            get_elevation='balita_stunting',  # Use 'elevation' column for elevation
            elevation_scale=100,  # You can adjust this value as needed
            # Set your desired elevation range
            elevation_range='[min_stunting, max_stunting]',
            extruded=True,
            coverage=1,
        ),
    ],
))
