import streamlit as st
import pandas as pd
import pydeck as pdk
import requests

# Mengambil data dari URL
url = "https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten"
response = requests.get(url)
data = response.json()

# Mengonversi data ke dalam bentuk dataframe
df = pd.DataFrame(data["data"])

# Menampilkan nama kota/kabupaten di Streamlit
st.write("Data Nama Kota/Kabupaten:")
st.write(df["bps_kota_nama"])

# Membuat peta dengan tanda pada setiap kota/kabupaten
layer = pdk.Layer(
    "TextLayer",
    data=df,
    get_position=["longitude", "latitude"],
    get_text="bps_kota_nama",
    get_color=[0, 255, 0, 255],  # Warna teks (hijau)
    get_size=30,
    get_alignment_baseline="bottom",
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
