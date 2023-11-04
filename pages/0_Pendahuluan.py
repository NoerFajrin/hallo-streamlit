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

    # Define a function to get color based on 'Nilai'
    def get_color(value):
        if value <= 20:
            return [0, 255, 0, 160]  # Green
        elif value <= 50:
            return [255, 255, 0, 160]  # Yellow
        else:
            return [255, 0, 0, 160]  # Red

    # Add a 'color' column to the sorted_df
    sorted_df['color'] = sorted_df['Nilai'].apply(get_color)

    # Create a PyDeck map with markers and text labels
    view_state = pdk.ViewState(
        latitude=sorted_df['Latitude'].mean(),
        longitude=sorted_df['Longitude'].mean(),
        zoom=9,
        pitch=50,
    )

    # Create a text label layer for 'Country and areas'
    text_layer_negara = pdk.Layer(
        'TextLayer',
        data=sorted_df,
        get_position='[Longitude, Latitude]',
        get_text='Country and areas',
        get_size=15,
        get_color='[0, 0, 0, 255]',
        get_alignment_baseline='bottom',
    )

    # Create a column layer with scaled 'Nilai' and color mapping
    column_layer = pdk.Layer(
        'ColumnLayer',
        data=sorted_df,
        get_position='[Longitude, Latitude]',
        get_fill_color='color',
        get_radius=200,
        auto_highlight=True,
        pickable=True,
        get_elevation='Nilai',
        elevation_scale=100,
        elevation_range=[0, 100],
        extruded=True,
        coverage=1,
    )

    # Create a PyDeck Deck with all layers
    deck = pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        layers=[text_layer_negara, column_layer],
        initial_view_state=view_state,
        tooltip={"html": "<b>Nilai:</b> {Nilai} <br><b>Negara:</b> {Country and areas} <br>",
                 "style": {"color": "white"}},
    )

    # Display the PyDeck map
    st.pydeck_chart(deck)
else:
    st.write("Data not found or could not be loaded.")
