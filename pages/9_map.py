import streamlit as st
import pydeck as pdk
import pandas as pd  # Pastikan Anda mengimpor pandas

# Koordinat Bandung
bandung_latitude = -6.9175
bandung_longitude = 107.6191

# Buat DataFrame dengan data Bandung
data = {
    'latitude': [bandung_latitude],
    'longitude': [bandung_longitude]
}
df = pd.DataFrame(data)  # Gunakan pd.DataFrame untuk membuat DataFrame

# Create a layer for the heatmap
heatmap_layer = pdk.Layer(
    'ScatterplotLayer',
    df,
    opacity=0.9,
    get_position=['longitude', 'latitude'],
    get_color=[0, 255, 0, 160],  # Warna hijau
    get_radius=200,
)

# Set the initial view state for the map (untuk melihat seluruh Indonesia)
view_state = pdk.ViewState(
    latitude=0,
    longitude=120,
    zoom=4,
    min_zoom=3,
    max_zoom=15,
    pitch=40.5,
    bearing=-80
)

# Create a PyDeck map
deck = pdk.Deck(
    layers=[heatmap_layer],
    initial_view_state=view_state
)

# Display the map
st.pydeck_chart(deck)
