import streamlit as st
import pandas as pd
import pydeck as pdk
import requests

# Endpoint untuk data kota/kabupaten di Provinsi Jawa Barat
endpoint = 'https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten'

# Mengambil data dari endpoint
response = requests.get(endpoint)
data = response.json().get('data', [])
st.write(data)
# Membuat DataFrame dengan data kota/kabupaten
df = pd.DataFrame(data)

# Ambil latitude dan longitude dari DataFrame
latitudes = df['latitude'].astype(float)
longitudes = df['longitude'].astype(float)
kota_nama = df['bps_kota_nama']

# Buat DataFrame dengan data latitude dan longitude
chart_data = pd.DataFrame({'lat': latitudes, 'lon': longitudes})

# Set initial view untuk fokus ke Jawa Barat
center_latitude = -6.920434
center_longitude = 107.604953

# Tambahkan layer untuk warna (misalnya, marker)
marker_layer = pdk.Layer(
    'ScatterplotLayer',
    data=chart_data,
    get_position='[lon, lat]',
    get_color=[0, 0, 255, 160],  # Warna biru
    get_radius=200,
)

# Tambahkan layer untuk teks (nama kota/kabupaten)
text_layer = pdk.Layer(
    'TextLayer',
    data=chart_data,
    get_position='[lon, lat]',
    get_text='kota_nama',  # Menampilkan teks nama kota/kabupaten
    get_size=20,  # Ukuran teks
    get_color=[0, 0, 0, 255],  # Warna teks
)

# Buat peta dengan dua layer terpisah
st.write(
    pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=center_latitude,
            longitude=center_longitude,
            zoom=8,
            pitch=50,
        ),
        layers=[marker_layer, text_layer],
    ),
    use_container_width=True,
    height=800
)
