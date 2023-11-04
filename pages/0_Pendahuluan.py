import streamlit as st
import pandas as pd

# Load the CSV data
datadunia = pd.read_csv('datadunia.csv')

# Check if the data has been loaded
if datadunia is not None:
    # Replace ',' with '.' in all columns of the DataFrame
    datadunia = datadunia.replace(',', '.', regex=True)

    # Extract Longitude (lon) and Latitude (lat) from "Data Awal"
    datadunia['Longitude'] = datadunia['Data Awal'].str.extract(
        r'Longitude \(lon\) = ([\d.-]+)')
    datadunia['Latitude'] = datadunia['Data Awal'].str.extract(
        r'Latitude \(lat\) = ([\d.-]+)')

    # Filter the years (2000-2022)
    selected_year_label = "Pilih Tahun"
    selected_year = st.selectbox(selected_year_label, list(range(2000, 2023)))

    # Rename the columns in the DataFrame
    datadunia = datadunia.rename(columns={
        "Country and areas": "Negara",
        str(selected_year): "Estimate",
        "Latitude": "lat",
        "Longitude": "lon"
    })

    # Select only the relevant columns
    selected_cols = ["Negara", "Estimate", "lat", "lon"]

    # Filter and sort the DataFrame
    sorted_df = datadunia[selected_cols].sort_values(
        by=str(selected_year), ascending=False)

    # Reset the index to start from 1 for the first row
    sorted_df = sorted_df.reset_index(drop=True)
    sorted_df.index += 1  # Start the index from 1

    # Display the sorted DataFrame with the modified column names and the modified index
    st.write(sorted_df)
else:
    st.write("Data not found or could not be loaded.")
