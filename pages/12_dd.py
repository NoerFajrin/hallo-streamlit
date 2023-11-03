import streamlit as st
import pydeck as pdk
import pandas as pd

CPU_GRID_LAYER_DATA = (
    "https://raw.githubusercontent.com/uber-common/"
    "deck.gl-data/master/website/sf-bike-parking.json"
)

st.title("GridLayer Example")

# Load the data
df = pd.read_json(CPU_GRID_LAYER_DATA)

# Define a layer to display on a map
layer = pdk.Layer(
    "GridLayer",
    df,
    pickable=True,
    extruded=True,
    cell_size=200,
    elevation_scale=4,
    get_position="COORDINATES",
)

view_state = pdk.ViewState(
    latitude=37.7749295,
    longitude=-122.4194155,
    zoom=11,
    bearing=0,
    pitch=45,
)

# Render the PyDeck map using Streamlit
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={
                "text": "{position}\nCount: {count}"}))
