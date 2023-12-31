import streamlit as st
import pandas as pd
import pydeck as pdk
import requests
import numpy as np

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
st.write(df)
json_array = df.to_json(orient='records')
# Display the JSON array
st.json(json_array)

# Filter DataFrame for the selected year
filtered_data = df[df['tahun'] == selected_year]
# Convert the 'tahun' and 'balita_stunting' columns to strings
filtered_data['tahun'] = filtered_data['tahun'].astype(str)
filtered_data['balita_stunting'] = filtered_data['balita_stunting'].astype(int)

# Min-max scaling function


def min_max_scaling(x, min_val, max_val, new_min, new_max):
    return ((x - min_val) / (max_val - min_val)) * (new_max - new_min) + new_min


# Calculate the minimum and maximum values of 'balita_stunting'
min_stunting = filtered_data['balita_stunting'].min()
max_stunting = filtered_data['balita_stunting'].max()

# Define the desired range (0 to 100)
new_min = 0
new_max = 100

# Apply min-max scaling to 'balita_stunting' and store the scaled values in a new column 'scaled_balita_stunting'
filtered_data['scaled_balita_stunting'] = filtered_data['balita_stunting'].apply(
    lambda x: min_max_scaling(x, min_stunting, max_stunting, new_min, new_max))

# Define a function to map scaled values to colors


def get_color(scaled_value):
    if scaled_value <= 20:
        return [0, 255, 0, 160]  # Green
    elif scaled_value <= 50:
        return [255, 255, 0, 160]  # Yellow
    else:
        return [255, 0, 0, 160]  # Red


# Add a 'color' column to the filtered_data
filtered_data['color'] = filtered_data['scaled_balita_stunting'].apply(
    get_color)

# Create a PyDeck map with markers and text labels
view_state = pdk.ViewState(
    latitude=filtered_data['lat'].mean(),
    longitude=filtered_data['lon'].mean(),
    zoom=9,
    pitch=50,
)

# Create a text label layer for 'scaled_balita_stunting'
text_layer_scaled_balita_stunting = pdk.Layer(
    'TextLayer',
    data=filtered_data,
    get_position='[lon, lat]',
    get_text='scaled_balita_stunting',
    get_size=15,
    get_color='[0, 0, 0, 255]',
    get_alignment_baseline="'bottom'",
)

# Create a text label layer for 'nama_kab'
text_layer_nama_kab = pdk.Layer(
    'TextLayer',
    data=filtered_data,
    get_position='[lon, lat]',
    get_text='nama_kab',
    get_size=15,
    get_color='[0, 0, 0, 255]',
    get_alignment_baseline="'bottom'",
)

# Create a column layer with scaled 'balita_stunting' and color mapping
column_layer = pdk.Layer(
    'ColumnLayer',
    data=filtered_data,
    get_position='[lon, lat]',
    get_fill_color='color',
    get_radius=200,
    auto_highlight=True,
    pickable=True,
    get_elevation='scaled_balita_stunting',
    elevation_scale=100,
    elevation_range=[0, 100],
    extruded=True,
    coverage=1,
)

# Create a PyDeck Deck with all layers
deck = pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=filtered_data,
            get_position='[lon, lat]',
            get_radius=200,
            get_color='[0, 0, 255, 160]'
        ),
        # //text_layer_scaled_balita_stunting,
        # text_layer_nama_kab,
        column_layer
    ],
    initial_view_state=view_state,
    tooltip={"html": "<b>Balita Stunting:</b> {balita_stunting} <br><b>Wilayah:</b> {nama_kab} <br>",
             "style": {"color": "white"}},
)
# Display the PyDeck map
st.pydeck_chart(deck)
