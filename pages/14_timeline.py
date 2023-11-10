import streamlit as st
import plotly.express as px
import pandas as pd

# Contoh data untuk timeline
data = {
    "Event": ["Event 1", "Event 2", "Event 3"],
    "Start Date": ["2023-01-01", "2023-02-01", "2023-03-01"],
    "End Date": ["2023-01-10", "2023-02-15", "2023-03-05"]
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
st.title("Timeline App")
st.plotly_chart(plot_timeline(df))
