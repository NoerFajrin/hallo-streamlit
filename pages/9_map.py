import streamlit as st
import pandas as pd
import pydeck as pdk
import requests

# Fetch location data
url_location = "https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten"
response_location = requests.get(url_location)
data_location = response_location.json()

# Convert location data to a DataFrame
df_location = pd.DataFrame(data_location["data"])

# Replace "Unknown Type: float" with suitable numeric values for latitude and longitude
for entry in df_location:
    if entry["latitude"] == "Unknown Type: float":
        entry["latitude"] = 0  # Replace with the correct latitude value
    if entry["longitude"] == "Unknown Type: float":
        entry["longitude"] = 0  # Replace with the correct longitude value

# Fetch additional data with "jumlah_balita_stunting"
url_stunting = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota?limit=300"
response_stunting = requests.get(url_stunting)
data_stunting = response_stunting.json()

# Convert the additional data to a DataFrame
df_stunting = pd.DataFrame(data_stunting["data"])

# Filter the additional data for the "tahun" you want (replace 'year_value' with the actual year)
year_value = "2023"  # Replace with the desired year
df_stunting_filtered = df_stunting[df_stunting["tahun"] == year_value]

# Merge the location data with the filtered additional data using "nama_kabupaten_kota" as the common key
merged_data = df_location.merge(
    df_stunting_filtered, left_on="bps_kota_nama", right_on="nama_kabupaten_kota", how="left")

# Create a map with points for each location
layer = pdk.Layer(
    "ScatterplotLayer",
    data=merged_data,
    get_position=["longitude", "latitude"],
    get_radius=1000,  # Point size
    get_fill_color=[0, 255, 0],  # Green color for points
    pickable=True,
)

# Create a layer for text labels
text_layer = pdk.Layer(
    "TextLayer",
    data=merged_data,
    get_position=["longitude", "latitude"],
    get_text="bps_kota_nama",
    get_size=20,
    get_color=[0, 0, 0],
    pickable=True,
)

view_state = pdk.ViewState(
    latitude=merged_data["latitude"].mean(),
    longitude=merged_data["longitude"].mean(),
    zoom=5,
)

r = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    layers=[layer, text_layer],
    initial_view_state=view_state,
)

st.title("Peta Data Balita Stunting di Jawa Barat")

st.pydeck_chart(r)
