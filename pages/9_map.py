import streamlit as st
import pandas as pd
import pydeck as pdk
import requests

# Define the API endpoint
endpoint_data_stunting = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota?limit=300"
endpoint_data_lat_lon = 'https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten'
# Make a GET request to the API
response = requests.get(endpoint_data_lat_lon)
responseStunting = requests.get(endpoint_data_stunting)
data = response.json().get('data', [])
# Membuat DataFrame dengan data kota/kabupaten
df = pd.DataFrame(data)
# Ambil latitude dan longitude dari DataFrame
latitudes = df['latitude'].astype(float)
longitudes = df['longitude'].astype(float)
# Replace "nama" with your actual column name containing location names
nama = df['bps_kota_nama'].astype('string')
# Buat DataFrame dengan data latitude dan longitude
chart_data = pd.DataFrame({'lat': latitudes, 'lon': longitudes, 'nama': nama})
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
                get_text="nama",
                get_color=[0, 0, 0, 255],
                get_size=9,  # Increase the font size
                get_alignment_baseline="'bottom'",
            ),
        ],
    ),
    use_container_width=True,
    height=800
)
