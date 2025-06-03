import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Respons Spektrum - SNI 1726:2019")

st.title("Respons Spektrum Berdasarkan SNI 1726:2019")
st.markdown("Lokasi: **Bujur 124.778151, Lintang 1.435556**")

Ss = 1.072598
S1 = 0.477211

site_classes = {
    "Kelas A": (0.8, 0.8),
    "Kelas B": (0.9, 0.9),
    "Kelas C": (1.0, 1.0),
    "Kelas D": (1.2, 1.2),
    "Kelas E": (1.4, 1.5),
}

site_class = st.selectbox("Pilih Kelas Situs:", list(site_classes.keys()))
Fa, Fv = site_classes[site_class]

SMS = Ss * Fa
SM1 = S1 * Fv

TL = 6  # Batas periode panjang

T = np.linspace(0, 4, 400)
Sa = []

for t in T:
    if t < 0.2 * SM1 / SMS:
        Sa.append(SMS * (0.4 + 3 * t / (0.2 * SM1 / SMS)))
    elif t <= SM1 / SMS:
        Sa.append(SMS)
    elif t <= TL:
        Sa.append(SM1 / t)
    else:
        Sa.append(SM1 * TL / (t ** 2))

Sa = np.array(Sa)

fig, ax = plt.subplots()
ax.plot(T, Sa, label=f"Kelas Situs: {site_class}")
ax.set_title("Kurva Respons Spektrum")
ax.set_xlabel("Periode (detik)")
ax.set_ylabel("Percepatan Spektral (g)")
ax.grid(True)
ax.legend()
st.pyplot(fig)
