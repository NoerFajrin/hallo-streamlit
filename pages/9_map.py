import streamlit as st
import pandas as pd
import geopandas as gpd
import pydeck as pdk

# Ambil data geometri wilayah (GeoJSON) dari sumber yang sesuai
# Misalnya, simpan dalam file seperti "wilayah_jawa_barat.geojson" dan baca dengan geopandas
wilayah_gdf = gpd.read_file("wilayah_jawa_barat.geojson")

# Pastikan kolom 'luas' dalam GeoDataFrame sesuai dengan luas wilayah
# Jika tidak ada kolom luas, Anda dapat menghitungnya dengan: wilayah_gdf['luas'] = wilayah_gdf.geometry.area

# Merge data kabupaten/kota dengan data geometri wilayah
# Pastikan ada kolom yang sesuai antara data dan data geometri (biasanya kolom 'id' atau 'kode')
kabupaten_data = pd.read_json("https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten")
merged_data = wilayah_gdf.merge(kabupaten_data, left_on='id', right_on='id', how='inner')

# Buat peta dengan Pydeck
st.write(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=merged_data["latitude"].mean(),
            longitude=merged_data["longitude"].mean(),
            zoom=7,
        ),
        layers=[
            pdk.Layer(
                "PolygonLayer",
                data=merged_data,
                get_polygon="geometry",
                get_fill_color="[luas * 2, 255 - luas * 2, 0, 150]",
                get_line_color=[0, 0, 0, 255],
                get_line_width=100,
                pickable=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=merged_data,
                get_position="[longitude, latitude]",
                get_color="[255, 0, 0, 200]",
                get_radius=200,
            ),
        ],
    ),
    use_container_width=True,
    height=800
)
