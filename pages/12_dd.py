import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# Generate random data
np.random.seed(0)
chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

# Display the random data
st.write(chart_data)

# Create a PyDeck map
view_state = pdk.ViewState(
    latitude=37.76,
    longitude=-122.4,
    zoom=11,
    pitch=50,
)

hexagon_layer = pdk.Layer(
    'HexagonLayer',
    data=chart_data,
    get_position='[lon, lat]',
    radius=200,
    elevation_scale=4,
    elevation_range=[0, 1000],
    pickable=True,
    extruded=True,
)

scatterplot_layer = pdk.Layer(
    'ScatterplotLayer',
    data=chart_data,
    get_position='[lon, lat]',
    get_color='[200, 30, 0, 160]',
    get_radius=200,
)

# Create a PyDeck Deck with the layers
deck = pdk.Deck(
    initial_view_state=view_state,
    layers=[hexagon_layer, scatterplot_layer],
    map_style="mapbox://styles/mapbox/light-v9",  # You can adjust the map style
)

# Display the PyDeck map in Streamlit
st.pydeck_chart(deck)
