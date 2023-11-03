import streamlit as st
import pandas as pd

# Load the CSV data
datadunia = pd.read_csv('datadunia.csv')

# Check if the data has been loaded
if datadunia is not None:
    # Split the 'data awal' column into 'Longitude (lon)' and 'Latitude (lat)'
    datadunia[['Longitude (lon)', 'Latitude (lat)']] = datadunia['data awal'].str.extract(
        r'Longitude \(lon\) = ([^;]+); Latitude \(lat\) = ([^)]+)')

    # Print the updated DataFrame
    st.write(datadunia)
else:
    st.write("Data not found or could not be loaded.")
