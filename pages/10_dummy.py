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

# Ambil latitude dan longitude dari DataFrame
tahun = df['tahun'].astype(int)
latitudes = df['latitude'].astype(float)
longitudes = df['longitude'].astype(float)
nama = df['nama_kab'].astype('string')
jumlah = df['balita_stunting'].astype(int)
# Buat DataFrame dengan data latitude dan longitude
chart_data = pd.DataFrame(
    {'lat': latitudes, 'lon': longitudes, 'jumlah': jumlah})
# Display the combined data
st.write(df)
# Set initial view for a more zoomed-in map
center_latitude = -6.920434
center_longitude = 107.604953
# Create a map with blue markers and text labels from the 'nama' column
st.write(
    pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=center_latitude,
            longitude=center_longitude,
            zoom=10,  # Adjust the zoom level as needed
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[0, 0, 255, 160]',  # Ensure the color is visible
                get_radius=200,
            ),
            pdk.Layer(
                "TextLayer",
                data=chart_data,
                get_position='[lon, lat]',
                get_text="jumlah",
                get_color=[0, 0, 0, 255],
                get_size=9,  # Increase the font size
                get_alignment_baseline="'bottom'",
            ),
        ],
    ),
    use_container_width=True,
    height=800
)
