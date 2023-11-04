import streamlit as st
import pandas as pd
import pydeck as pdk

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

    # Convert "Latitude" and "Longitude" columns to numeric (float)
    datadunia['Latitude'] = pd.to_numeric(
        datadunia['Latitude'], errors='coerce')
    datadunia['Longitude'] = pd.to_numeric(
        datadunia['Longitude'], errors='coerce')

    # Filter the years (2000-2022)
    st.write("# Unicef Data: Monitoring the situation of Children and Woman")
    st.write("Noer Fajrin, 23222036")
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

    # Display the sorted DataFrame with the modified index
    st.write(sorted_df)

    # Create a PyDeck map
    view_state = pdk.ViewState(
        latitude=0,  # Provide the default latitude here
        longitude=0,  # Provide the default longitude here
        zoom=1,  # Provide the default zoom level here
    )

    # Create a text layer for 'Country and areas' with tooltips
    text_layer = pdk.Layer(
        "TextLayer",
        data=sorted_df,
        get_position=["Longitude", "Latitude"],
        get_text="Country and areas",
        get_size=24,
        get_color=[255, 0, 0],
        get_alignment_baseline="'bottom'",
    )

    # Create a PyDeck Deck with the text layer and view state
    deck = pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        layers=[text_layer],
        initial_view_state=view_state,
        tooltip={"html": "<b>Country:</b> {Country and areas}",
                 "style": {"color": "white"}},
    )

    # Display the PyDeck map
    st.pydeck_chart(deck)
else:
    st.write("Data not found or could not be loaded.")
