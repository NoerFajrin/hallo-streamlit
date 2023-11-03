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

    # Add a new column for row number
    datadunia['Row Number'] = range(1, len(datadunia) + 1)

    # Print the updated DataFrame
    st.write(datadunia)

    # Filter the years (2000-2022)
    selected_years = st.selectbox("Select Year", list(range(2000, 2023)))

    # Select only the relevant columns
    selected_cols = ["Row Number", "Country and areas", str(
        selected_years), "Latitude", "Longitude"]

    # Filter and sort the DataFrame
    sorted_df = datadunia[selected_cols].sort_values(
        by=str(selected_years), ascending=False)

    # Get the number of rows to display
    num_rows = st.number_input(
        "Number of Rows to Display", min_value=1, value=10)

    # Display the sorted DataFrame with the selected number of rows
    st.dataframe(sorted_df.head(num_rows), index=False)
else:
    st.write("Data not found or could not be loaded.")
