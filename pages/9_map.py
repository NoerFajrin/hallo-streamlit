import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# URL APIs
api_url1 = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota?limit=300"
api_url2 = "https://data.jabarprov.go.id/api-backend/bigdata/bps/od_20000_indeks_kedalaman_kemiskinan_berdasarkan_kabupatenkota?limit=1000&where=%7B%22tahun%22%3A%5B%222014%22%2C%222015%22%2C%222016%22%2C%222017%22%2C%222018%22%2C%222019%22%2C%222020%22%2C%222021%22%2C%222022%22%5D%7D"

# Fungsi untuk mendapatkan data dari API
def get_api_data(api_url):
    response = requests.get(api_url)
    return response.json()

# Set the title for the page
st.title("Data Visualizations for Jawa Barat")

# Fetch data from the first API
data1 = get_api_data(api_url1)

# Fetch data from the second API
data2 = get_api_data(api_url2)

# Create a list of unique years for both datasets
if "data" in data1:
    df1 = pd.DataFrame(data1["data"])
    years1 = sorted(df1["tahun"].unique())

if "data" in data2:
    df2 = pd.DataFrame(data2["data"])
    years2 = sorted(df2["tahun"].unique())

# Check if the first API response is valid
if "data" in data1:
    st.header("Grafik Data Balita Stunting di Jawa Barat")

    # Select a year using a widget
    selected_year1 = st.selectbox("Pilih Tahun Data Balita Stunting:", years1)

    # Filter data1 based on the selected year
    filtered_data1 = df1[df1["tahun"] == selected_year1]

    # Create a bar chart for data1
    fig1 = px.bar(
        filtered_data1,
        x="nama_kabupaten_kota",
        y="jumlah_balita_stunting",
        title=f"Jumlah Balita Stunting di Jawa Barat Tahun {selected_year1}",
        labels={"jumlah_balita_stunting": "Jumlah Balita Stunting", "nama_kabupaten_kota": "Kabupaten/Kota"}
    )

    # Display the bar chart for data1
    st.plotly_chart(fig1)
else:
    st.write("Tidak ada data untuk Data Balita Stunting.")

# Check if the second API response is valid
if "data" in data2:
    st.header("Peta Indeks Kemiskinan di Jawa Barat")

    # Select a year using a widget
    selected_year2 = st.selectbox("Pilih Tahun Indeks Kemiskinan:", years2)

    # Filter data2 based on the selected year
    filtered_data2 = df2[df2["tahun"] == selected_year2]

    # Create a choropleth map for data2
    fig2 = px.choropleth(
        filtered_data2,
        geojson="https://data.jabarprov.go.id/api-backend/geospatial/vl2022kabkota",
        featureidkey="properties.ID",
        locations="id_kabupatenkota",
        color="indeks_kedalaman_kemiskinan",
        color_continuous_scale="Viridis",
        labels={"indeks_kedalaman_kemiskinan": "Indeks Kemiskinan"},
        title=f"Indeks Kemiskinan di Jawa Barat Tahun {selected_year2}",
    )
    # Display the choropleth map for data2
    st.plotly_chart(fig2)
else:
    st.write("Tidak ada data untuk Indeks Kemiskinan.")
