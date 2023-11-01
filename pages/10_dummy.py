import streamlit as st
import pydeck as pdk
import pandas as pd

# Sample data with latitude, longitude, and labels
data = [
    {'lat': 37.7749, 'lon': -122.4194, 'name': 'RinRin'},
    {'lat': 34.0522, 'lon': -118.2437, 'name': 'Juna'},
    {'lat': 40.7128, 'lon': -74.0060, 'name': 'New York'},
]

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Create a map centered on the United States with a higher zoom level
st.write(
    pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=39.8097,
            longitude=-98.5556,
            zoom=5,  # Adjust the zoom level as needed
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[0, 0, 255, 160]',  # Blue color
                get_radius=20000,
                get_text='name',  # Display the 'name' column as text labels
                get_size=3000,
            ),
        ],
    ),
    use_container_width=True,
    height=800
)
