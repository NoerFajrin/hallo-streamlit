import streamlit as st
import pandas as pd
import pydeck as pdk

chart_data = pd.DataFrame(
    columns=['lat', 'lon']
)

# Specify the latitude and longitude of Indonesia
indonesia_latitude = -2.4833826
indonesia_longitude = 117.8902853

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=indonesia_latitude,
        longitude=indonesia_longitude,
        zoom=5,  # You can adjust the zoom level
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=chart_data,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
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
