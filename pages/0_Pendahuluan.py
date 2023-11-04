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
        r'Longitude \(lon\) = ([\d.-]+)').astype(float)
    datadunia['Latitude'] = datadunia['Data Awal'].str.extract(
        r'Latitude \(lat\) = ([\d.-]+)').astype(float)
    # Filter the years (2000-2022)
    selected_years = st.selectbox("Select Year", list(range(2000, 2023)))
    # Select only the relevant columns
    selected_cols = ["Country and areas", str(
        selected_years), "Latitude", "Longitude"]
    # Filter and sort the DataFrame
    sorted_df = datadunia[selected_cols].sort_values(
        by=str(selected_years), ascending=False)
    # Reset the index to start from 1 for the first row
    sorted_df = sorted_df.reset_index(drop=True)
    sorted_df.index += 1  # Start the index from 1
    # Display the sorsted DataFrame with the modified index
    st.write(sorted_df)

    json_array = sorted_df.to_json(orient='records')

    # Display the JSON array
    st.json(json_array)
else:
    st.write("Data not found or could not be loaded.")
