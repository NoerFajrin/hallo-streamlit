import streamlit as st
import pandas as pd

# Load the CSV data
datadunia = pd.read_csv('datadunia.csv')

# Check if the data has been loaded
if datadunia is not None:
    # Print the DataFrame
    st.write(datadunia)
else:
    st.write("Data not found or could not be loaded.")
