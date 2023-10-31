import streamlit as st
import pydeck as pdk

DATA_SOURCE = 'https://raw.githubusercontent.com/ajduberstein/geo_datasets/master/fortune_500.csv'

layer = pdk.Layer(
    "HeatmapLayer",
    DATA_SOURCE,
    opacity=0.9,
    get_position=["longitude", "latitude"],
    aggregation="'MEAN'",
    get_weight="profit / employees > 0 ? profit / employees : 0"
)

view_state = pdk.ViewState(
    longitude=-95.7129,
    latitude=37.0902,
    zoom=3,
    min_zoom=2,
    max_zoom=15,
    pitch=40.5,
    bearing=-80
)

r = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state
)

r.to_html("heatmap.html")
