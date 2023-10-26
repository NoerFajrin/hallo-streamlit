import streamlit as st
import pandas as pd
import pydeck as pdk
import requests

# Ambil data kabupaten/kota dari API
api_url = "https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten"
response = requests.get(api_url)
data = response.json()
kabupaten_data = data.get("data")

# Buat DataFrame dari data kabupaten/kota
df = pd.DataFrame(kabupaten_data)

# Buat peta dengan Pydeck
st.write(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=df["latitude"].mean(),
            longitude=df["longitude"].mean(),
            zoom=7,
        ),
        layers=[
            pdk.Layer(
                "PolygonLayer",
                data=df,
                get_polygon="[longitude, latitude]",
                get_fill_color="[nilai * 2, 255 - nilai * 2, 0, 150]",
                get_line_color=[0, 0, 0, 255],
                get_line_width=100,
                pickable=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position="[longitude, latitude]",
                get_color="[255, 0, 0, 200]",
                get_radius=200,
            ),
        ],
    ),
    use_container_width=True,
    height=800
)
