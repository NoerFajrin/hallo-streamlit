import streamlit as st
import pandas as pd
import pydeck as pdk

# Load the CSV data


def get_color(nilai):
    if nilai <= 20:
        return [0, 0, 255, 160]  # Blue
    elif nilai <= 50:
        return [255, 255, 0, 160]  # Yellow
    else:
        return [255, 0, 0, 160]  # Red


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
            "Nilai": int(row[str(selected_years)]),
            "Negara": row["Country and areas"],
            "lat": row["Latitude"],
            "lon": row["Longitude"]
        }
        new_json_array.append(new_json_item)

    # Display the new JSON array
    st.json(new_json_array)
    df = pd.DataFrame(new_json_array)

    # Apply the get_color function to each element in the 'Nilai' column
    df['FillColor'] = df['Nilai'].apply(get_color)
    # Extract latitude and longitude coordinates from the DataFrame
    coordinates = [(row["lon"], row["lat"]) for index, row in df.iterrows()]

    # Create a list of connections to form a ring
    connections = []

    # Append connections for the ring
    for i in range(len(coordinates)):
        connections.append({
            "start": coordinates[i],
            "end": coordinates[(i + 1) % len(coordinates)]
        })

    # Create a PyDeck map with markers and text labels
    view_state = pdk.ViewState(
        latitude=4.2105,  # Set latitude to a central point in Southeast Asia
        longitude=101.9758,  # Set longitude to a central point in Southeast Asia
        zoom=4,  # Adjust the zoom level as needed to encompass the desired region
        pitch=50,
    )

    # Create a text label layer for 'nama_kab'
    great_circle_layer = pdk.Layer(
        "GreatCircleLayer",
        data=connections,
        get_source_position="start",
        get_target_position="end",
        get_stroke_width=2,
        get_source_color=[255, 0, 0],
        get_target_color=[0, 0, 255],
    )
    text_layer_nama_negara = pdk.Layer(
        'TextLayer',
        data=df,
        get_position='[lon, lat]',
        get_text='Negara',
        get_size=30,
        get_color='[0, 0, 0, 255]',
        get_alignment_baseline="'bottom'",
    )

    # Create a column layer with scaled 'balita_stunting' and color mapping
    column_layer = pdk.Layer(
        'ColumnLayer',
        data=df,
        get_position='[lon, lat]',
        get_fill_color='FillColor',
        get_radius=500000000,
        auto_highlight=True,
        pickable=True,
        get_elevation='Nilai',
        elevation_scale=10000,
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
                data=df,
                get_position='[lon, lat]',
                get_radius=200,
                get_color='[0, 0, 255, 160]'
            ),
            # text_layer_nama_negara,
            # great_circle_layer,
            column_layer
        ],
        initial_view_state=view_state,
        tooltip={"html": "<b>Estimate Value :</b> {Nilai} <br><b>Wilayah:</b> {Negara} <br>",
                 "style": {"color": "white"}},
    )
    # Display the PyDeck map
    st.pydeck_chart(deck)
else:
    st.write("Data not found or could not be loaded.")
