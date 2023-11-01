import streamlit as st
import pydeck as pdk
import pandas as pd

# Create a DataFrame with dummy data for one point
data = pd.DataFrame({
    'latitude': [37.7749],
    'longitude': [-122.4194],
    'text': ['My home'],
    'text_color': [255, 0, 0],  # Red color for text
    # Green color for circle (with alpha value for transparency)
    'circle_color': [0, 255, 0, 150]
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
            get_color='text_color',  # Set text color
            get_background_color='circle_color',  # Set circle color
        ),
    ],
))

st.write("Text added to the map at (latitude, longitude): 37.7749, -122.4194")
