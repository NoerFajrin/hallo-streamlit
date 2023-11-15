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

# Normalize "Jumlah Balita Stunting" values to be within the range of 0 to 5
if "data" in data1:
    df1["jumlah_balita_stunting"] = (df1["jumlah_balita_stunting"] - df1["jumlah_balita_stunting"].min()) / (
        df1["jumlah_balita_stunting"].max() - df1["jumlah_balita_stunting"].min()) * 5

# Normalize "Indeks Kemiskinan" values to be within the range of 0 to 5
if "data" in data2:
    df2["indeks_kedalaman_kemiskinan"] = (df2["indeks_kedalaman_kemiskinan"] - df2["indeks_kedalaman_kemiskinan"].min()) / (
        df2["indeks_kedalaman_kemiskinan"].max() - df2["indeks_kedalaman_kemiskinan"].min()) * 5

# Check if the first API response is valid
if "data" in data1:
    st.header("Grafik Data Balita Stunting dan Indeks Kemiskinan di Jawa Barat")

    # Select a year using a widget
    selected_year1 = st.selectbox("Pilih Tahun Data Balita Stunting:", years1)

    # Filter data1 based on the selected year
    filtered_data1 = df1[df1["tahun"] == selected_year1]

    # Filter data2 based on the selected year
    filtered_data2 = df2[df2["tahun"] == selected_year1]

    # Create a line chart for data1 with red color
    fig = px.line(
        filtered_data1,
        x="nama_kabupaten_kota",
        y="jumlah_balita_stunting",
        title=f"Jumlah Balita Stunting dan Indeks Kemiskinan di Jawa Barat Tahun {selected_year1}",
        labels={
            "jumlah_balita_stunting": "Jumlah Balita Stunting (Normalized)", "nama_kabupaten_kota": "Kabupaten/Kota"}
    )

    # Add a line chart for data2 with green color
    fig.add_scatter(
        x=filtered_data2["nama_kabupaten_kota"],
        y=filtered_data2["indeks_kedalaman_kemiskinan"],
        mode="lines",
        line=dict(color="green"),
        name="Indeks Kemiskinan (Normalized)"
    )

    # Display the combined line chart
    st.plotly_chart(fig)
else:
    st.write("Tidak ada data untuk Data Balita Stunting dan Indeks Kemiskinan.")
st.write("\n")  # Ini akan menambahkan satu baris kosong
st.write("\n")  # Ini akan menambahkan satu baris kosong
st.write("Berdasarkan grafik diatas, dapat disimpulkan bahwa, Kemiskinan bukan menjadi faktor utama dalam kasus Stunting.")
