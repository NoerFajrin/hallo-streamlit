import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image

# Contoh data untuk timeline
data = {
    "Aktivitas": ["Perancangan", "Perakitan", "Uji Coba", "Analisis & Kesimpulan"],
    "Tanggal Mulai": ["2023-04-01", "2023-05-01", "2023-09-01", "2023-10-01"],
    "Tanggal Selesai": ["2023-05-01", "2023-09-01", "2023-10-01", "2023-11-01"]
}

df = pd.DataFrame(data)
df['Tanggal Mulai'] = pd.to_datetime(df['Tanggal Mulai'])
df['Tanggal Selesai'] = pd.to_datetime(df['Tanggal Selesai'])

# Fungsi untuk membuat timeline


def plot_timeline(data):
    fig = px.timeline(data, x_start="Tanggal Mulai",
                      x_end="Tanggal Selesai", y="Aktivitas", title="Timeline")
    return fig


# Tampilkan aplikasi Streamlit
st.title("Timeline Kerja Sama")
st.plotly_chart(plot_timeline(df))
st.write("\n")  # Ini akan menambahkan satu baris kosong
st.write("\n")  # Ini akan menambahkan satu baris kosong
st.title("- Perancanga")
image1 = Image.open("aset/perancangan.png")
st.image(image1)
image2 = Image.open("aset/perancangan1.png")
st.image(image2)
image3 = Image.open("aset/perancangan2.png")
st.image(image3)
