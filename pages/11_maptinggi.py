import pydeck as pdk
import streamlit as st

UK_ACCIDENTS_DATA = 'https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv'

layer = pdk.Layer(
    'HexagonLayer',
    UK_ACCIDENTS_DATA,
    get_position=['lng', 'lat'],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1)

view_state = pdk.ViewState(
    longitude=-1.415,
    latitude=52.2323,
    zoom=6,
    min_zoom=5,
    max_zoom=15,
    pitch=40.5,
    bearing=-27.36)

st.title("3D Hexagon Heatmap Example")

# Display the PyDeck map using st.pydeck_chart
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

# Optionally, you can save the HTML output for the visualization
st.markdown("You can also save the visualization as an HTML file:")
st.markdown(
    "[Download hexagon-example.html](sandbox:/path/to/hexagon-example.html)")
