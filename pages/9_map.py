import streamlit as st
import pandas as pd
import pydeck as pdk
import requests

# Define the API endpoint
api_endpoint = 'https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten'

# Make a GET request to the API
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Display the data in the Streamlit app
    st.title('API Data Display')
    st.write('Data from the API:')
    st.write(data)
else:
    st.error(
        f'Failed to retrieve data from the API. Status code: {response.status_code}')

# You can add more Streamlit components to format the output as needed
# Mengambil data dari endpoint
data = response.json().get('data', [])

# Membuat DataFrame dengan data kota/kabupaten
df = pd.DataFrame(data)

# Ambil latitude dan longitude dari DataFrame
latitudes = df['latitude'].astype(float)
longitudes = df['longitude'].astype(float)

# Buat DataFrame dengan data latitude dan longitude
chart_data = pd.DataFrame({'lat': latitudes, 'lon': longitudes})

# Set initial view untuk fokus ke Jawa Barat
center_latitude = -6.920434
center_longitude = 107.604953

# Buat peta dengan tanda biru di semua kota/kabupaten
st.write(
    pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=center_latitude,
            longitude=center_longitude,
            zoom=8,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[0, 0, 255, 160]',  # Warna biru
                get_radius=200,
                get_text='text',
            ),
        ],
    ),
    use_container_width=True,
    height=800
)
