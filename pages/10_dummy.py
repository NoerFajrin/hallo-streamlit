import pandas as pd
import streamlit as st
import pydeck as pdk

data = pd.DataFrame({
    'latitude': [37.7749, 37.785, 37.793],
    'longitude': [-122.4194, -122.395, -122.408],
    'text': ['Point 1', 'Point 2', 'Point 3'],
    'text_color': [[255, 0, 0], [0, 0, 255], [0, 255, 0]],
    'circle_color': [[0, 255, 0, 150], [255, 0, 0, 150], [0, 0, 255, 150]]
})

st.header("My PyDeck Map")

# Layer pertama untuk warna lokasi
layer_location = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position=["longitude", "latitude"],
    get_fill_color="circle_color",
    get_radius=100,
    pickable=True,
    auto_highlight=True,
)

# Layer kedua untuk nomor
data['number'] = [1, 2, 3]
layer_number = pdk.Layer(
    "TextLayer",
    data=data,
    get_position=["longitude", "latitude"],
    get_text="number",
    get_color=[0, 0, 0],
    get_size=25,
    get_alignment_baseline="'bottom'",
)

# Layer ketiga untuk dot color
layer_dot_color = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position=["longitude", "latitude"],
    get_fill_color="text_color",
    get_radius=100,
    pickable=True,
    auto_highlight=True,
)

# Membuat peta
view_state = pdk.ViewState(
    latitude=data['latitude'].mean(),
    longitude=data['longitude'].mean(),
    zoom=8,
)
r = pdk.Deck(layers=[layer_location, layer_number,
             layer_dot_color], initial_view_state=view_state)

# Menampilkan peta menggunakan komponen Streamlit
st.pydeck_chart(r)
