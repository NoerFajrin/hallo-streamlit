import streamlit as st
import pandas as pd
import pydeck as pdk

chart_data = pd.DataFrame(
    columns=['lat', 'lon']
)

# Specify the latitude and longitude for Aceh and Papua
aceh_latitude = 4.2266
aceh_longitude = 96.7494
papua_latitude = -4.2699
papua_longitude = 138.0804

# Calculate the midpoint for the initial view
center_latitude = (aceh_latitude + papua_latitude) / 2
center_longitude = (aceh_longitude + papua_longitude) / 2

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=center_latitude,
        longitude=center_longitude,
        zoom=4,  # Adjust the zoom level as needed
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=chart_data,
            get_position='[lon, lat]',
            radius=200,
            # elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))
