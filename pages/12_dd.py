import streamlit as st
import pydeck as pdk
import pandas as pd

# Create a DataFrame with dummy data (latitude, longitude, and elevation)
data = pd.DataFrame({
    'lat': [37.7749, 37.7749, 37.775, 37.7751],
    'lon': [-122.4194, -122.4184, -122.42, -122.42],
    'elevation': [10, 30, 60, 90]
})

# Create a PyDeck map
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=data['lat'].mean(),
        longitude=data['lon'].mean(),
        zoom=15,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=data,
            get_position='[lon, lat]',
            get_radius=200,
            get_fill_color='[0, elevation, 0]',
            pickable=True,
            extruded=True,
            elevation_scale=4,
        ),
    ],
))
