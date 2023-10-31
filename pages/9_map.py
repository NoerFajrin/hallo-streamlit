import streamlit as st
import pandas as pd
import pydeck as pdk
import requests

# Mengambil data dari URL
url = "https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten"
response = requests.get(url)
data = response.json()

# Mengganti "Unknown Type: float" dengan nilai numerik yang sesuai
for entry in data["data"]:
    if entry["latitude"] == "Unknown Type: float":
        entry["latitude"] = 0  # Ganti dengan nilai latitude yang sesuai
    if entry["longitude"] == "Unknown Type: float":
        entry["longitude"] = 0  # Ganti dengan nilai longitude yang sesuai

# Mengonversi data ke dalam bentuk dataframe
df = pd.DataFrame(data["data"])

# Membuat peta dengan titik di setiap latlon
layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_text=":baby:",
    get_position=["longitude", "latitude"],
    get_radius=1000,  # Ukuran titik
    get_fill_color=[0, 255, 0],  # Warna titik (hijau)
    pickable=True,
)

view_state = pdk.ViewState(
    latitude=df["latitude"].mean(),
    longitude=df["longitude"].mean(),
    zoom=5,
)

r = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    layers=[layer],
    initial_view_state=view_state,
)

st.pydeck_chart(r)
