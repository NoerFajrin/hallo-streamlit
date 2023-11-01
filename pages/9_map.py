import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster

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

# Create a map centered on Jawa Barat
m = folium.Map(location=[-6.920434, 107.604953], zoom_start=8)

# Create a MarkerCluster for grouping markers
marker_cluster = MarkerCluster().add_to(m)

# Add markers with custom text
for index, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup="Ini lokasi terpilih",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(marker_cluster)

# Display the map in Streamlit
st.write(m)
