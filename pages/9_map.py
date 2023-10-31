import streamlit as st
import requests
import pandas as pd
import pydeck as pdk

# URL API for Balita Stunting data
api_url_stunting = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota?limit=300"

# Function to get Balita Stunting data from the API


def get_api_data(api_url):
    response = requests.get(api_url)
    return response.json()

# Function to fetch location data


def get_location_data():
    url = "https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten"
    response = requests.get(url)
    data = response.json()

    # Replace "Unknown Type: float" with suitable numeric values
    for entry in data["data"]:
        if entry["latitude"] == "Unknown Type: float":
            entry["latitude"] = 0  # Replace with the correct latitude value
        if entry["longitude"] == "Unknown Type: float":
            entry["longitude"] = 0  # Replace with the correct longitude value

    return pd.DataFrame(data["data"])


# Fetch Balita Stunting data and location data
stunting_data = get_api_data(api_url_stunting)
location_data = get_location_data()

st.title("Tabel Data Balita Stunting di Jawa Barat")

# Check if the API response is valid
if "data" in stunting_data:
    st.write(
        "Berikut ini adalah Tabel Data Stunting di Provinsi Jawa Barat dari Tahun 2014 - 2021")

    # Create a list of unique years from the data and sort it
    years = sorted(list(set(item['tahun'] for item in stunting_data["data"])))

    # Select a year using the widget
    selected_year = st.selectbox("Pilih Tahun:", years)

    # Create a list for the table based on the selected year
    table_data = []
    for item in stunting_data["data"]:
        if item['tahun'] == selected_year:
            row = {
                "Kabupaten/Kota": item['nama_kabupaten_kota'],
                "Jumlah Balita Stunting": item['jumlah_balita_stunting'],
                "Tahun": item['tahun']
            }
            table_data.append(row)

    # Display data in a table
    st.table(table_data)
else:
    st.write("Tidak ada data yang tersedia.")

# Create a map with location data and balita stunting data
st.title("Peta Data Balita Stunting di Jawa Barat")

# Merge the location data with the balita stunting data
merged_data = pd.merge(
    location_data, stunting_data["data"], left_on="bps_kota_nama", right_on="nama_kabupaten_kota", how="inner")

# Create a map with points for each location
layer = pdk.Layer(
    "ScatterplotLayer",
    data=merged_data,
    get_position=["longitude", "latitude"],
    # Use the number of stunted children to determine the radius
    get_radius="jumlah_balita_stunting",
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

map_chart = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    layers=[layer, text_layer],  # Add text layer
    initial_view_state=view_state,
)

st.pydeck_chart(map_chart)
