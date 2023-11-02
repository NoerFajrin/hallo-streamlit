import pydeck as pdk
import streamlit as st

# Create a DataFrame from the provided coordinates
import pandas as pd

data = {
    'lng': [-0.198465, -0.178838, -0.205590, -0.208327],
    'lat': [51.505538, 51.491836, 51.514910, 51.514952]
}

df = pd.DataFrame(data)

# Create a PyDeck layer using the provided data
layer = pdk.Layer(
    'HexagonLayer',
    df,
    get_position=['lng', 'lat'],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1
)

view_state = pdk.ViewState(
    longitude=-0.2,
    latitude=51.5,
    zoom=12,
    min_zoom=5,
    max_zoom=15,
    pitch=40.5,
    bearing=-27.36
)

st.title("Custom 3D Hexagon Heatmap Example")

# Display the PyDeck map using st.pydeck_chart
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
