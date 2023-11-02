import streamlit as st
import requests
import pandas as pd
import pydeck as pdk

# Define the API endpoints
endpoint_data_stunting = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota?limit=300"
endpoint_data_lat_lon = 'https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten'

# Make GET requests to the APIs
response = requests.get(endpoint_data_lat_lon)
responseStunting = requests.get(endpoint_data_stunting)

# Parse the JSON responses
data_lat_lon = response.json().get('data', [])
data_stunting = responseStunting.json().get('data', [])

# Create a list of years for selection and sort it
years = sorted(list(set(stunting_data["tahun"]
               for stunting_data in data_stunting)))

# Allow the user to select a year
selected_year = st.selectbox("Select a year", years)

# Create data for each layer
data_layers = []

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

            data_layers.append({
                "nama_kab": nama_kabupaten_kota_stunting,
                "lat": lat,
                "lon": lon,
                "jumlah_stunting": jumlah_balita_stunting
            })

# Create Pandas DataFrame for the combined data
data_df = pd.DataFrame(data_layers)

# Display the combined data with 3 layers on the map
st.pydeck_chart(
    pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=data_df['lat'].mean(),
            longitude=data_df['lon'].mean(),
            zoom=8,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=data_df,
                get_position='[lon, lat]',
                get_radius='jumlah_stunting / 100',  # Adjust radius as needed
                get_fill_color=[0, 0, 255, 160],
            ),
            pdk.Layer(
                "TextLayer",
                data=data_df,
                get_position='[lon, lat]',
                get_text="jumlah_stunting",
                get_color=[0, 0, 0, 255],
                get_size=16,
                get_alignment_baseline="'top'",
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=data_df,
                get_position='[lon, lat]',
                get_radius=200,
                get_fill_color=[255, 0, 0, 160],
            ),
        ],
    ),
    use_container_width=True,
)
