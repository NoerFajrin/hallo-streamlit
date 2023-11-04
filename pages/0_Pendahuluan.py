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

    # Create a new data format
    data_baru = {
        # Convert to list
        "nama_negara": sorted_df["Country and areas"].tolist(),
        "lat": sorted_df["Latitude"].tolist(),  # Convert to list
        "lon": sorted_df["Longitude"].tolist(),  # Convert to list
        "prediksi": sorted_df[selected_years].tolist(),  # Convert to list
    }

    # Use data_baru for the map
    st.write("New Data Format for Map:")
    st.write(data_baru)

    # Create a PyDeck map using data_baru
    view_state = pdk.ViewState(
        latitude=0,  # Provide the default latitude here
        longitude=0,  # Provide the default longitude here
        zoom=1,  # Provide the default zoom level here
    )

    # Create a text layer for 'nama_negara' with tooltips
    text_layer = pdk.Layer(
        "TextLayer",
        data=data_baru,
        get_position=["lon", "lat"],
        get_text="nama_negara",
        get_size=24,
        get_color=[255, 0, 0],
        get_alignment_baseline="'bottom'",
    )

    # Create a PyDeck Deck with the text layer and view state
    deck = pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        layers=[text_layer],
        initial_view_state=view_state,
        tooltip={"html": "<b>Country:</b> {nama_negara}",
                 "style": {"color": "white"}},
    )

    # Display the PyDeck map
    st.pydeck_chart(deck)

else:
    st.write("Data not found or could not be loaded.")
