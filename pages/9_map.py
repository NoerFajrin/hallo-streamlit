import streamlit as st
import requests

# Define the API endpoint
api_endpoint = 'https://data.jabarprov.go.id/api-backend/bigdata/diskominfo/od_kode_wilayah_dan_nama_wilayah_kota_kabupaten'

# Make a GET request to the API
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Display the data in the Streamlit app
    st.title('API Data Display')
    st.write('Data from the API:')
    st.write(data)
else:
    st.error(
        f'Failed to retrieve data from the API. Status code: {response.status_code}')

# You can add more Streamlit components to format the output as needed
