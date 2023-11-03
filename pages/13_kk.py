import streamlit as st
import pandas as pd

# Load the CSV data
datadunia = pd.read_csv('datadunia.csv')

# Check if the data has been loaded
if datadunia is not None:
    # Replace ',' with '.' in all columns of the DataFrame
    datadunia = datadunia.replace(',', '.', regex=True)

    # Mengekstrak Longitude (lon) dan Latitude (lat) dari "Data Awal"
    datadunia['Longitude'] = datadunia['Data Awal'].str.extract(
        r'Longitude \(lon\) = ([\d.-]+)')
    datadunia['Latitude'] = datadunia['Data Awal'].str.extract(
        r'Latitude \(lat\) = ([\d.-]+)')

    # Print the updated DataFrame
    st.write(datadunia)

    # Pilih tahun untuk mengurutkan
    selected_year = st.selectbox("Pilih Tahun", datadunia.columns[:-3])

    # Urutkan DataFrame berdasarkan tahun yang dipilih
    sorted_df = datadunia.sort_values(by=selected_year, ascending=False)

    # Tampilkan DataFrame yang telah diurutkan
    st.write(sorted_df)
else:
    st.write("Data not found or could not be loaded.")
