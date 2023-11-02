import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# Generate random data with elevation values
chart_data = pd.DataFrame({
    'lat': np.random.uniform(37.75, 37.77, 1000),  # Adjust latitude range
    'lon': np.random.uniform(-122.45, -122.42, 1000),  # Adjust longitude range
    'elevation': np.random.randint(0, 1000, 1000)  # Elevation values
})

st.write(chart_data)

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
            get_elevation='elevation',  # Use 'elevation' column for elevation
            elevation_scale=4,  # You can adjust this value as needed
            elevation_range=[0, 1000],  # Set your desired elevation range
            extruded=True,
            coverage=1
        ),
    ],
))
