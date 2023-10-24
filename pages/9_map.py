import streamlit as st
import pydeck as pdk

# Data peta (contoh data)
data = [
    {'lat': 37.7749, 'lon': -122.4194, 'name': 'San Francisco'},
    {'lat': 34.0522, 'lon': -118.2437, 'name': 'Los Angeles'},
    {'lat': 40.7128, 'lon': -74.0060, 'name': 'New York City'},
]

# Membuat peta dengan pdk.Deck
view_state = pdk.ViewState(
    latitude=data[0]['lat'],
    longitude=data[0]['lon'],
    zoom=6
)

layer = pdk.Layer(
    'ScatterplotLayer',
    data=data,
    get_position='[lon, lat]',
    get_radius=1000,
    get_color=[255, 0, 0],
    pickable=True,
    auto_highlight=True
)

# Menampilkan peta dalam aplikasi Streamlit
st.title("Contoh Peta dengan pdk.Deck")
st.pydeck_chart(pdk.Deck(
    initial_view_state=view_state,
    layers=[layer]
))
