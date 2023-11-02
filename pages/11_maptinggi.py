import numpy as np
import pandas as pd
import pydeck as pdk

import streamlit as st

chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)


height = st.slider("Height", 100, 1000, 500)

chart = pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=chart_data,
            get_position="[lon, lat]",
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
        ),
        pdk.Layer(
            "ScatterplotLayer",
            data=chart_data,
            get_position="[lon, lat]",
            get_color="[200, 30, 0, 160]",
            get_radius=200,
        ),
    ],
    height=height,  # Set the height of the map
)

# Pass the height to the frame
st.components.v1.html(chart.to_html(as_string=True), height=height)
