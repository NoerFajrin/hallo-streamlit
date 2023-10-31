import streamlit as st
import pandas as pd
import pydeck as pdk
import requests

# Mengambil data dari URL
url = "https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten"
response = requests.get(url)
data = response.json()

# Access the data appropriately
latitude = data["data"]["latitude"]
longitude = data["data"]["longitude"]
bps_kota_nama = data["data"]["bps_kota_nama"]

# Create a DataFrame
df = pd.DataFrame(
    {"latitude": latitude, "longitude": longitude, "bps_kota_nama": bps_kota_nama})

# Membuat peta dengan titik di setiap latlon
layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position=["longitude", "latitude"],
    get_radius=1000,  # Ukuran titik
    get_fill_color=[0, 255, 0],  # Warna titik (hijau)
    pickable=True,
)

# Membuat layer untuk teks label
text_layer = pdk.Layer(
    "TextLayer",
    data=df,
    get_position=["longitude", "latitude"],
    get_text="bps_kota_nama",
    get_size=20,
    get_color=[0, 0, 0],
    pickable=True,
)

view_state = pdk.ViewState(
    latitude=latitude.mean(),
    longitude=longitude.mean(),
    zoom=5,
)

r = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    layers=[layer, text_layer],  # Tambahkan layer teks
    initial_view_state=view_state,
)

st.pydeck_chart(r)
