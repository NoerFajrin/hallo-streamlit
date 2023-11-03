import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# Create a slider for chart height
height = st.slider('Chart height:', 0, 500, 400, 100)

# Generate random data
data = np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4]
df = pd.DataFrame(data, columns=["lat", "lon"])
st.write(df)
# Create a PyDeck HexagonLayer
hexagon_layer = pdk.Layer(
    "HexagonLayer",
    data=df,
    get_position="[lon, lat]",
    radius=200,
    elevation_scale=4,
    elevation_range=[0, 1000],
    pickable=True,
    extruded=True,
)

# Create a PyDeck ScatterplotLayer
scatterplot_layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position="[lon, lat]",
)

# Create a PyDeck Deck with the layers
deck = pdk.Deck(
    layers=[hexagon_layer, scatterplot_layer],
    initial_view_state={
        "latitude": 37.76,
        "longitude": -122.4,
        "zoom": 11,
        "pitch": 50,
        "height": height,
    },
    map_style="mapbox://styles/mapbox/light-v9",  # You can adjust the map style
)

# Display the PyDeck map in Streamlit
st.pydeck_chart(deck)
