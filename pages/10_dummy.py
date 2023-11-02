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

# Filter DataFrame for the selected year
filtered_data = df[df['tahun'] == selected_year]
st.write(filtered_data)
tipe_data_tahun = filtered_data['balita_stunting'].dtype
st.write("Tipe data kolom 'tahun':", tipe_data_tahun)
# Mengubah tipe data kolom 'tahun' menjadi objek (string)
filtered_data['tahun'] = filtered_data['tahun'].astype(str)

# Menampilkan DataFrame yang telah diubah
st.write(filtered_data)


# Create a PyDeck map with markers and text labels using the "balita_stunting" column as text
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=filtered_data['lat'].mean(),
        longitude=filtered_data['lon'].mean(),
        zoom=6,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=filtered_data,
            get_position='[lon, lat]',
            get_radius=1000,  # Adjust the marker size as needed
            get_color='[0, 0, 255, 160]',  # Marker color (blue)
        ),
        pdk.Layer(
            'TextLayer',
            data=filtered_data,
            get_position='[lon, lat]',
            get_text='tahun',
            get_size=18,  # Text label size
            get_color='[0, 0, 0, 255]',  # Text label color (black)
        ),
    ],
))
