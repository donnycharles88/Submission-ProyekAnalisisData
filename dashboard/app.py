import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="Dashboard Bike Sharing", layout="wide")

# Judul Dashboard
st.title("Dashboard Analisis Bike Sharing")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv('dashboard/day.csv')

df_day = load_data()

# Sidebar Filter
st.sidebar.header("Filter Data")
year = st.sidebar.selectbox("Pilih Tahun", options=df_day['yr'].unique())
season = st.sidebar.selectbox("Pilih Musim", options=df_day['season'].unique())

# Filter Dataframe
df_filtered = df_day[(df_day['yr'] == year) & (df_day['season'] == season)]

# Menampilkan Metric Utama
total_rentals = df_filtered['cnt'].sum()
total_casual = df_filtered['casual'].sum()
total_registered = df_filtered['registered'].sum()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan", f"{total_rentals:,}")
with col2:
    st.metric("Pengguna Casual", f"{total_casual:,}")
with col3:
    st.metric("Pengguna Registered", f"{total_registered:,}")

st.markdown("---")

# Visualisasi 1: Rata-rata Penyewaan per Musim
st.subheader("1. Rata-Rata Penyewaan Sepeda per Musim")
fig1, ax1 = plt.subplots(figsize=(10, 6))
season_avg = df_day.groupby('season')['cnt'].mean()
season_labels = ['Spring', 'Summer', 'Fall', 'Winter']
sns.barplot(x=season_labels, y=season_avg.values, ax=ax1, palette='viridis')
ax1.set_title('Rata-Rata Penyewaan Sepeda per Musim')
ax1.set_xlabel('Musim')
ax1.set_ylabel('Rata-Rata Jumlah Penyewaan')
st.pyplot(fig1)

# Visualisasi 2: Tren Penyewaan per Bulan
st.subheader("2. Tren Penyewaan per Bulan")
fig2, ax2 = plt.subplots(figsize=(10, 6))
month_avg = df_day.groupby('mnth')['cnt'].mean()
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax2.plot(month_labels, month_avg.values, marker='o', linewidth=2, color='skyblue')
ax2.set_title('Tren Penyewaan Sepeda per Bulan')
ax2.set_xlabel('Bulan')
ax2.set_ylabel('Rata-Rata Jumlah Penyewaan')
ax2.grid(axis='y', alpha=0.3)
st.pyplot(fig2)

# Visualisasi 3: Komposisi Pengguna (Casual vs Registered)
st.subheader("3. Komposisi Total Pengguna (Casual vs Registered)")
fig3, ax3 = plt.subplots(figsize=(8, 6))
total_casual = df_day['casual'].sum()
total_registered = df_day['registered'].sum()
sizes = [total_registered, total_casual]
labels = [f'Registered\n{total_registered:,}', f'Casual\n{total_casual:,}']
colors = ['#4ECDC4', '#FF6B6B']
ax3.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax3.set_title('Komposisi Total Pengguna (2011-2012)')
st.pyplot(fig3)

# Kesimpulan
st.markdown("---")
st.subheader("Kesimpulan")
st.write("""
1. **Musim:** Penyewaan sepeda paling tinggi terjadi pada musim Fall (Musim Gugur) dan Summer (Musim Panas).
2. **Tren Bulanan:** Penyewaan cenderung meningkat pada pertengahan tahun (Mei - September).
3. **Pengguna:** Pengguna Registered mendominasi dibandingkan pengguna Casual, menunjukkan bahwa sebagian besar pengguna adalah pelanggan tetap.
""")
