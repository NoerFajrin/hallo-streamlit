import streamlit as st
import pydeck as pdk
import geopandas as gpd

# Baca data GeoJSON
geojson_data = gpd.read_file("geojson.geojson")  # Gantilah "path_to_geojson.geojson" dengan path ke file GeoJSON Anda

# Buat aplikasi Streamlit
st.title("Peta GeoJSON di Streamlit")

# Buat peta dengan Pydeck
st.write(
    pdk.Deck(
        layers=[
            pdk.Layer(
                "GeoJsonLayer",
                data=geojson_data,
                filled=True,
                extruded=True,
                get_fill_color=[0, 255, 0, 200],  # Warna wilayah diisi
                get_line_color=[0, 0, 0, 255],  # Warna garis batas wilayah
            )
        ],
    )
)
