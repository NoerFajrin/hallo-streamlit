import streamlit as st
import folium

# Set the title for the page
st.title("Peta Indonesia")

# Create a map centered on Indonesia
m = folium.Map(location=[-2.274897, 118.243141], zoom_start=5)

# Add a marker for a specific location (e.g., Jakarta)
folium.Marker([-6.2088, 106.8456], popup='Jakarta').add_to(m)

# Display the map in Streamlit
st.write(m)