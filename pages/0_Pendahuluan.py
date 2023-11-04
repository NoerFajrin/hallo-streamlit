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
    # Display the sorsted DataFrame with the modified index
    # st.write(sorted_df)

    json_array = sorted_df.to_json(orient='records')

    # Display the JSON array
    # st.json(json_array)
    new_json_array = []

    for index, row in sorted_df.iterrows():
        new_json_item = {
            "Nilai": row[str(selected_years)],
            "Negara": row["Country and areas"],
            "lat": row["Latitude"],
            "lon": row["Longitude"]
        }
        new_json_array.append(new_json_item)

    # Display the new JSON array
    st.json(new_json_array)

    # Create a PyDeck map with markers and text labels
    view_state = pdk.ViewState(
        latitude=-2.5489,  # Latitude of Indonesia
        longitude=118.0149,  # Longitude of Indonesia
        zoom=5,  # Adjust the zoom level as needed
        pitch=50,
    )

    # Create a text label layer for 'nama_kab'
    text_layer_nama_negara = pdk.Layer(
        'TextLayer',
        data=new_json_array,
        get_position='[lon, lat]',
        get_text='Negara',
        get_size=15,
        get_color='[0, 0, 0, 255]',
        get_alignment_baseline="'bottom'",
    )

    # Create a column layer with scaled 'balita_stunting' and color mapping
    column_layer = pdk.Layer(
        'ColumnLayer',
        data=new_json_array,
        get_position='[lon, lat]',
        get_fill_color='[0, 255, 0, 160]',
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
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=new_json_array,
                get_position='[lon, lat]',
                get_radius=200,
                get_color='[0, 0, 255, 160]'
            ),
            # //text_layer_scaled_balita_stunting,
            # text_layer_nama_kab,
            column_layer
        ],
        initial_view_state=view_state,
        tooltip={"html": "<b>Balita Stunting:</b> {Nilai} <br><b>Wilayah:</b> {Negara} <br>",
                 "style": {"color": "white"}},
    )
    # Display the PyDeck map
    st.pydeck_chart(deck)
else:
    st.write("Data not found or could not be loaded.")
