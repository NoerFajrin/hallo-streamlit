import streamlit as st
import pandas as pd
import pydeck as pdk
import requests

# URL to the GeoJSON file for Jawa Barat province
geojson_url = "https://raw.githubusercontent.com/hitamcoklat/Jawa-Barat-Geo-JSON/master/Jabar_By_Kab.geojson"

# Data that you want to visualize (replace this with your data)
data = pd.read_csv("data.csv")

# Create a GeoJSON layer
layer = pdk.Layer(
    "GeoJsonLayer",
    data=geojson_url,
    opacity=0.8,
    stroked=False,
    filled=True,
    extruded=False,
    get_fill_color=[128, 0, 128, 140],  # Purple color with transparency
    get_line_color=[0, 0, 0],
    pickable=True,
)

view_state = pdk.ViewState(
    latitude=-6.920000,  # Replace with the appropriate latitude
    longitude=107.600000,  # Replace with the appropriate longitude
    zoom=7,
    pitch=0,
)

# Show the map using Streamlit
st.pydeck_chart(pdk.Deck(map_style="mapbox://styles/mapbox/light-v9",
                layers=[layer], initial_view_state=view_state))
