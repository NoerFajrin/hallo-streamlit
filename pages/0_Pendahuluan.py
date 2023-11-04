import streamlit as st
import pandas as pd

# Load the CSV data
datadunia = pd.read_csv('datadunia.csv')

# Check if the data has been loaded
if datadunia is not None:
    # Replace ',' with '.' in all columns of the DataFrame
    datadunia = datadunia.replace(',', '.', regex=True)

    # Extract Longitude (lon) and Latitude (lat) from "Data Awal" and convert to float
    datadunia['Longitude'] = datadunia['Data Awal'].str.extract(
        r'Longitude \(lon\) = ([\d.-]+)')
    datadunia['Latitude'] = datadunia['Data Awal'].str.extract(
        r'Latitude \(lat\) = ([\d.-]+)')

    try:
        datadunia['Longitude'] = datadunia['Longitude'].astype(float)
        datadunia['Latitude'] = datadunia['Latitude'].astype(float)
    except ValueError as e:
        st.error(f"Error converting to float: {e}")

    # Filter the years (2000-2022)
    selected_years = st.selectbox("Select Year", list(range(2000, 2023)))

    # ... Rest of your code for sorting and displaying

else:
    st.write("Data not found or could not be loaded.")
