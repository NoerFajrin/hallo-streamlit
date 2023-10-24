import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# URL API for Balita Stunting data
api_url_stunting = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota?limit=300"

# URL API for Indeks Kemiskinan data
api_url_kemiskinan = "https://data.jabarprov.go.id/api-backend/bigdata/bps/od_20000_indeks_kedalaman_kemiskinan_berdasarkan_kabupatenkota?limit=1000&where=%7B%22tahun%22%3A%5B%222014%22%2C%222015%22%2C%222016%22%2C%222017%22%2C%222018%22%2C%222019%22%2C%222020%22%2C%222021%22%2C%222022%22%5D%7D"

# Function to get data from the API
def get_api_data(api_url):
    response = requests.get(api_url)
    return response.json()

# Display data in the form of graphs
st.title("Data in Jawa Barat")

# Select a year for both datasets
years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
selected_year = st.selectbox("Select Year:", years)

# Balita Stunting Data
st.subheader("Balita Stunting Data")

data_stunting = get_api_data(api_url_stunting)

# Check if the API response is valid
if "data" in data_stunting:
    st.write("Graph of the Number of Stunted Children in West Java")

    # Create a DataFrame from the data
    df_stunting = pd.DataFrame(data_stunting["data"])

    # Filter the data based on the selected year
    filtered_data_stunting = df_stunting[df_stunting["tahun"] == selected_year]

    # Create a bar chart
    fig_stunting = px.bar(
        filtered_data_stunting,
        x="nama_kabupaten_kota",
        y="jumlah_balita_stunting",
        title=f'Number of Stunted Children in West Java for the Year {selected_year}',
        labels={"jumlah_balita_stunting": "Number of Stunted Children", "nama_kabupaten_kota": "District/City"}
    )

    # Display the Stunting Children graph
    st.plotly_chart(fig_stunting)
else:
    st.write("No Stunting Children data available.")

# Indeks Kemiskinan Data
st.subheader("Indeks Kemiskinan Data")

data_kemiskinan = get_api_data(api_url_kemiskinan)

# Check if the API response is valid
if "data" in data_kemiskinan:
    st.write("Graph of Poverty Index:")

    # Create a list for the graph based on the selected year
    graph_data_kemiskinan = []
    for item in data_kemiskinan["data"]:
        if item['tahun'] == selected_year:
            row = {
                "Kabupaten/Kota": item['nama_kabupaten_kota'],
                "Indeks Kemiskinan": item['indeks_kedalaman_kemiskinan'],
            }
            graph_data_kemiskinan.append(row)

    # Convert data to a DataFrame
    df_kemiskinan = pd.DataFrame(graph_data_kemiskinan)

    # Create the Poverty Index graph using plotly
    fig_kemiskinan = px.bar(df_kemiskinan, x='Kabupaten/Kota', y='Indeks Kemiskinan', title=f'Poverty Index in West Java ({selected_year})')
    st.plotly_chart(fig_kemiskinan)
else:
    st.write("No Poverty Index data available.")
