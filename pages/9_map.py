import streamlit as st
import pandas as pd
import pydeck as pdk
import requests

# Endpoint untuk data kota/kabupaten di Provinsi Jawa Barat
endpoint = 'https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten'
# struktur data API
# {
#   "data": {
#     "bps_kota_kode": 0,
#     "bps_kota_nama": "string",
#     "bps_provinsi_kode": 0,
#     "bps_provinsi_nama": "string",
#     "id": 0,
#     "kemendagri_kota_kode": "Unknown Type: float",
#     "kemendagri_kota_nama": "string",
#     "kemendagri_provinsi_kode": 0,
#     "kemendagri_provinsi_nama": "string",
#     "kode_pos": "Unknown Type: float",
#     "latitude": "Unknown Type: float",
#     "longitude": "Unknown Type: float",
#     "status_adm": "string"
#   },
#   "error": 0,
#   "message": "string",
#   "metadata": {}
# }
# Mengambil data dari endpoint
response = requests.get(endpoint)
data = response.json().get('data', [])

# Membuat DataFrame dengan data kota/kabupaten
df = pd.DataFrame(data)

# Ambil latitude, longitude, dan nama kota/kabupaten dari DataFrame
latitudes = df['latitude'].astype(float)
longitudes = df['longitude'].astype(float)
kota_nama = df['bps_kota_nama'].astype('string')

# Buat DataFrame dengan data latitude, longitude, dan nama kota/kabupaten
chart_data = pd.DataFrame(
    {'lat': latitudes, 'lon': longitudes, 'kota_nama': kota_nama})

# Set initial view untuk fokus ke Jawa Barat
center_latitude = -6.920434
center_longitude = 107.604953

# Tambahkan ikon marker dengan teks nama kota/kabupaten
icon_layer = pdk.Layer(
    'IconLayer',
    data=chart_data,
    get_position='[lon, lat]',
    get_color=[0, 0, 255, 160],  # Warna biru
    get_text='kota_nama',  # Menampilkan teks nama kota/kabupaten
    get_text_size=20,  # Ukuran teks
    get_text_color=[0, 0, 0, 255],  # Warna teks
)

# Buat peta dengan ikon marker dan teks di setiap kota/kabupaten
st.write(
    pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=center_latitude,
            longitude=center_longitude,
            zoom=8,
            pitch=50,
        ),
        layers=[icon_layer],
    ),
    use_container_width=True,
    height=800
)
