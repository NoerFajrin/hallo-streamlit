# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="23222036",
        page_icon="👋",
    )

    st.write(
        "# Kerja Sama ITB dan PT. KIREI dalam Upaya Penurunan Prevalensi Stunting di Jawa Barat")
    st.write("Noer Fajrin, 23222036")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        ### Pendahuluan
        
        Indonesia merupakan negara dengan angka stunting tertinggi ke-2 di Asia Tenggara dan menduduki peringkat ke-5 di dunia menurut data riset kesehatan dasar (Riskesdas) di tahun 2018
       
         ### Rumusan Masalah dan Urgensi Kerja sama
         - Prevalensi stunting termasuk masalah gizi kronis. (Prevalensi Stunting adalah Jumlah balita di suatu populasi yang mengalami stunting dalam pertumbuhan fisiknya).
         - Proses pencatatan dan pemetaan tumbuh kembang anak di Indonesia belum sepenuhnya terdigitalisasi dan terintegrasi dengan alat ukur yang digunakan. 
         - 1000 hari pertama menentukan prevalensi stunting sangat penting untuk menangani agar tidak prevalensi stunting
         - Mendukung Program Pemerintah untuk menurunkan prevalensi stunting di 2024.
         - Membantu tenaga kesehatan dalam proses pencatatan, pemetaan, dan analisis tumbuh kembang anak.
         - Dapat menentukan prevalensi stunting di 1000 hari pertama sehingga dapat mempercepat penanganan atau pencegahan prevalensi stunting, 
         - Rekacipta yang dibuat mampu  mengakomodir proses pengukuran, penginputan, pemetaan dan menganalisis tumbuh kembang anak.

         ### Program Jawa Barat Zero Stunting 2024
         - Kepala Dinas Kesehatan dr. Nina Susana Dewi, Sp.PK(K)., M. Kes., MMRS., memaparkan data survei SSGI tahun 2021 yang mengatakan bahwa prevalensi stunting di Provinsi Jawa Barat dikategorikan tinggi pada tahun tersebut dan menargetkan Jabar zero new stunting pada 2023. Paparan tersebut dibahas pada rapat terbatas koordinasi evaluasi capaian kinerja triwulan II Dinkes tahun 2022 di Soreang Kabupaten Bandung, Selasa (7/6/2022).
         - Jabar Zero New Stunting adalah program unggulan Gubernur Jawa Barat dalam mendukung program nasional untuk menurunkan prevalensi stunting, dengan target capaian pada tahun 2023 adalah 19,2%.

    """
    )


if __name__ == "__main__":
    run()
