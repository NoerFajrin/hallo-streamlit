import streamlit as st
import plotly.express as px
import pandas as pd

# Contoh data untuk timeline
data = {
    "Event": ["Perancangan", "Perakitan", "Uji Coba", "Analisis & Kesimpulan"],
    "Start Date": ["2023-04-01", "2023-05-01", "2023-09-01", "2023-10-01"],
    "End Date": ["2023-05-01", "2023-09-15", "2023-10-05", "2023-11-01"]
}

df = pd.DataFrame(data)
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['End Date'] = pd.to_datetime(df['End Date'])

# Fungsi untuk membuat timeline


def plot_timeline(data):
    fig = px.timeline(data, x_start="Start Date",
                      x_end="End Date", y="Event", title="Timeline")
    return fig


# Tampilkan aplikasi Streamlit
st.title("Timeline Appp")
st.plotly_chart(plot_timeline(df))
