import streamlit as st
import pydeck as pdk
import pandas as pd

# Create a DataFrame with dummy data for multiple points
data = pd.DataFrame({
    'latitude': [37.7749, 37.785, 37.793],
    'longitude': [-122.4194, -122.395, -122.408],
    'text': ['Point 1', 'Point 2', 'Point 3'],
    # Red, Blue, Green colors for text
    'text_color': [[255, 0, 0], [0, 0, 255], [0, 255, 0]],
    # Green, Red, Blue circles (with alpha value for transparency)
    'circle_color': [[0, 255, 0, 150], [255, 0, 0, 150], [0, 0, 255, 150]]
})

# Create a Pydeck map
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=data['latitude'].mean(),
        longitude=data['longitude'].mean(),
        zoom=10,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            'TextLayer',
            data=data,
            get_position='[longitude, latitude]',
            get_text='text',
            get_size=16,
            get_color='text_color',
            get_background_color='circle_color',
        ),
    ],
))

st.write("Multiple points added to the map.")
