import streamlit as st
import pandas as pd
import requests
import pydeck as pdk

# Fungsi untuk mendapatkan data dari API


def get_api_data():
    url = "https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten"
    response = requests.get(url)
    data = response.json()
    return data


# Mendapatkan data dari API
api_data = get_api_data()

# Membuat list untuk latitude dan longitude
latitudes = [item['latitude'] for item in api_data]
longitudes = [item['longitude'] for item in api_data]

# Membuat dataframe dengan data latitude dan longitude
chart_data = pd.DataFrame({
    'lat': latitudes,
    'lon': longitudes
})

# Membuat peta
aceh_latitude = 4.2266
aceh_longitude = 96.7494
papua_latitude = -4.2699
papua_longitude = 138.0804

# Calculate the midpoint for the initial view
center_latitude = (aceh_latitude + papua_latitude) / 2
center_longitude = (aceh_longitude + papua_longitude) / 2

st.write(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=center_latitude,
            longitude=center_longitude,
            zoom=4,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[0, 255, 0, 160]',  # Warna hijau
                get_radius=200,
            ),
        ],
    ),
    use_container_width=True,
    height=800
)
