import streamlit as st
import pandas as pd
import pydeck as pdk

chart_data = pd.DataFrame(
    columns=['lat', 'lon']
)

# Calculate the midpoint for the initial view
center_latitude = (aceh_latitude + papua_latitude) / 2
center_longitude = (aceh_longitude + papua_longitude) / 2

# Use Streamlit's layout options to set the width and height of the map
st.write(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=center_latitude,
            longitude=center_longitude,
            zoom=4,  # Adjust the zoom level to show all of Indonesia
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=chart_data,
                get_position='[lon, lat]',
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ),
    use_container_width=True,  # Set width to the width of the Streamlit container
    height=800  # Set a custom height (adjust as needed)
)
