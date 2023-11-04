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
        latitude=filtered_data['lat'].mean(),
        longitude=filtered_data['lon'].mean(),
        zoom=9,
        pitch=50,
    )

    # Create a text label layer for 'balita_stunting'
    text_layer_balita_stunting = pdk.Layer(
        'TextLayer',
        data=filtered_data,
        get_position='[lon, lat]',
        get_text='balita_stunting',
        get_size=15,
        get_color='[0, 0, 0, 255]',
        get_alignment_baseline="'bottom'",
    )

    # Create a text label layer for 'nama_kab'
    text_layer_nama_kab = pdk.Layer(
        'TextLayer',
        data=filtered_data,
        get_position='[lon, lat]',
        get_text='nama_kab',
        get_size=15,
        get_color='[0, 0, 0, 255]',
        get_alignment_baseline="'bottom'",
    )

    # Create a PyDeck Deck with all layers
    deck = pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=view_state,
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=filtered_data,
                get_position='[lon, lat]',
                get_radius=1000,
                get_color='[0, 0, 255, 160]'
            ),
            text_layer_balita_stunting,
            text_layer_nama_kab,
            pdk.Layer(
                'HexagonLayer',
                data=filtered_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
                auto_highlight=True,
                pickable=True,
                get_elevation='balita_stunting',
                elevation_scale=5,
                elevation_range=[1000, 20000],
                extruded=True,
                coverage=1,
            )
        ]
    )

    # Display the PyDeck map
    st.pydeck_chart(deck)
else:
    st.write("Data not found or could not be loaded.")
