import streamlit as st
import pydeck as pdk
import pandas as pd

# Define view state for the map
view_state = pdk.ViewState(
    latitude=32,
    longitude=35,
    zoom=7,
    pitch=0
)

# Sample data
data = {
    'lon': [35, 35.1],
    'lat': [32.5, 32.6],
    'name': ['meA', 'meB'],
    'prec': [100, 300],
    'temp': [10, 30],
    'elevationValue': [100, 300]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the tooltip for data points
tooltip = {
    "html": "Name: {name}\nRain: {prec} mm",
    "style": {
        "backgroundColor": "steelblue",
        "color": "black"
    }
}

# Create a ScatterplotLayer
scatterplot_layer = pdk.Layer(
    type='ScatterplotLayer',
    data=df,
    get_position=["lon", "lat"],
    get_color=["255-temp", "31+temp", "31+temp*3"],
    get_line_color=[0, 0, 0],
    get_radius=1750,
    pickable=True,
    onClick=True,
    filled=True,
    line_width_min_pixels=10,
    opacity=2
)

# Create a TextLayer for displaying labels
text_layer = pdk.Layer(
    "TextLayer",
    df,
    pickable=False,
    get_position=["lon", "lat"],
    get_text="name",
    get_size=3000,
    sizeUnits='meters',
    get_color=[0, 0, 0],
    get_angle=0,
    getTextAnchor="middle",
    get_alignment_baseline="center"
)

# Create the PyDeck Deck
deck = pdk.Deck(
    initial_view_state=view_state,
    map_provider='mapbox',
    map_style=pdk.map_styles.SATELLITE,
    layers=[scatterplot_layer, text_layer],
    tooltip=tooltip
)

# Display the map in Streamlit
st.pydeck_chart(deck)
