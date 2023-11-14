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
        "# Kerja Sama ITB dan PT. KIREI dalam Penurunan Prevalensi Stunting di Jawa Barat")
    st.write("Noer Fajrin, 23222036")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
    ### Pendahuluan
    Indonesia merupakan negara dengan angka stunting tertinggi ke-2 di Asia Tenggara dan menduduki peringkat ke-5 di dunia menurut data riset kesehatan dasar (Riskesdas) di tahun 2018
        
    """
    )


if __name__ == "__main__":
    run()
