import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Respons Spektrum SNI 1726:2019", layout="wide")

# Judul
st.title("Respons Spektrum Desain (SNI 1726:2019)")
st.write("Lokasi: Lat 1.435556, Lon 124.778151")
st.write("SS=1.0726, S1=0.4772")

# Parameter gempa
Ss = 1.072598
S1 = 0.477211
TL = 6.0  # Periode panjang default

# Faktor kelas situs (SNI 1726:2019 Tabel 5)
site_classes = {
    "Kelas A": (0.8, 0.8),
    "Kelas B": (0.9, 0.9),
    "Kelas C": (1.0, 1.0),
    "Kelas D": (1.2, 1.2),
    "Kelas E": (1.4, 1.5),
}

# Generate kurva
T = np.linspace(0.001, 4, 400)
fig, ax = plt.subplots(figsize=(10, 6))

for kelas, (Fa, Fv) in site_classes.items():
    SMS = Ss * Fa
    SM1 = S1 * Fv
    TS = SM1 / SMS
    T0 = 0.2 * TS

    Sa = []
    for t in T:
        if t < T0:
            Sa.append(SMS * (0.4 + 0.6 * t / T0))  # Naik linear
        elif t <= TS:
            Sa.append(SMS)  # Datar
        elif t <= TL:
            Sa.append(SM1 / t)  # Turun 1/t
        else:
            Sa.append(SM1 * TL / (t ** 2))  # Turun 1/t²

    ax.plot(T, Sa, label=kelas)

# Format plot
ax.set_title("Respons Spektrum Desain (SNI 1726:2019)\nLokasi: Lat 1.435556, Lon 124.778151\nSS=1.0726, S1=0.4772")
ax.set_xlabel("Periode (detik)")
ax.set_ylabel("Percepatan Spektral (g)")
ax.grid(True)
ax.legend(title="Kelas Situs")

# Tampilkan grafik di Streamlit
st.pyplot(fig)
