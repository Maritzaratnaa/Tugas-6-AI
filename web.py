'''
Nama    : Maritza Ratnamaya N.
NPM     : 140810230076
Kelas   : B
'''

import streamlit as st
from sklearn.cluster import KMeans
from PIL import Image
import numpy as np


def getWarna(image, n_warna = 5):
    gambar = image.resize((150, 150))
    gambar_np = np.array(gambar)
    gambar_np = gambar_np.reshape(-1, 3)
    
    kmeans = KMeans(n_clusters=n_warna)
    kmeans.fit(gambar_np)
    warna = kmeans.cluster_centers_.astype(int)
 
    return warna

st.set_page_config(page_title="Color Palette Picker", layout="centered")
st.markdown("""
    <style>
    .color-info {
        font-size: 13px;
        margin-top: 4px;
        text-align: center;
    }
    </style>
    
    <h1 style="text-align: center;">
    <span style="color: #black; font-style: italic;">Palette</span> 
    <span style="color: #black; font-style: italic;">Color</span> 
    <span style="color: #fd362d; background-color: #ffe6e6; padding: 4px 8px; ">PICKER</span>
    </h1>
    <p style="text-align: center;"> Generator untuk membantu menentukan 5 warna dominan dari sebuah gambar</p>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    gambar = Image.open(uploaded_file)
    st.image(gambar, use_container_width=True)
    
    with st.spinner("Proses..."):
        warna = getWarna(gambar)
        st.markdown("""
            <h2>
                <span style="color: #black; font-style: italic;">Color Palette</span>
            </h2>
        """, unsafe_allow_html=True)

        cols = st.columns(len(warna))

        for i, (c, col) in enumerate(zip(warna, cols)):
            rgb = tuple(int(x) for x in c)
            hex_warna = '#%02x%02x%02x' % rgb
            with col:
                st.markdown(f"""
                    <div style='text-align: center'>
                        <input type='color' value='{hex_warna}' style='width: 60px; height: 60px; border: none; cursor: default;' disabled>
                        <div style='margin-top: 5px; font-size: 13px;'>RGB: {rgb}<br>HEX: {hex_warna}</div>
                    </div>
                """, unsafe_allow_html=True)