import streamlit as st
import requests
import matplotlib.pyplot as plt

# URL API
api_url = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_17147_jumlah_balita_stunting_berdasarkan_kabupatenkota"

# Fungsi untuk mendapatkan data dari API
def get_api_data():
    response = requests.get(api_url)
    return response.json()

# Tampilkan data dalam bentuk grafik
st.title("Data Balita Stunting di Jawa Barat")

data = get_api_data()

# Periksa apakah respon API valid
if "data" in data:
    st.write("Data Balita Stunting:")

    # Buat daftar untuk grafik
    kabupaten_kota = []
    years = []
    jumlah_stunting = []

    for item in data["data"]:
        nama_kabupaten_kota = item.get('nama_kabupaten_kota', 'Kabupaten/Kota Tidak Valid')
        try:
            tahun = int(item['tahun'])
        except (ValueError, TypeError):
            tahun = 'Tahun Tidak Valid'
        jumlah_stunting_value = item.get('jumlah_balita_stunting', 0)

        kabupaten_kota.append(nama_kabupaten_kota)
        years.append(tahun)
        jumlah_stunting.append(jumlah_stunting_value)

    # Buat grafik batang untuk setiap kota berdasarkan tahun
    for i, kota in enumerate(kabupaten_kota):
        plt.figure(figsize=(10, 6))
        plt.bar(years[i], jumlah_stunting[i])
        plt.xlabel('Tahun')
        plt.ylabel('Jumlah Balita Stunting')
        plt.title(f'Grafik Jumlah Balita Stunting di {kota}')
        st.write(f'Grafik Jumlah Balita Stunting di {kota}')
        st.pyplot(plt)

else:
    st.write("Tidak ada data yang tersedia.")
