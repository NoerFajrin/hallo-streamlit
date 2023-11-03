import streamlit as st
import pandas as pd

# Load the CSV data
datadunia = pd.read_csv('datadunia.csv')

# Check if the data has been loaded
if datadunia is not None:
    # Replace ',' with '.' in all columns of the DataFrame
    datadunia = datadunia.replace(',', '.', regex=True)

    # Print the DataFrame
    st.write(datadunia)

    # Convert DataFrame to JSON and display it
    st.json(datadunia.to_json(orient='records'))
else:
    st.write("Data not found or could not be loaded.")
