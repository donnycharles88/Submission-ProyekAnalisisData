import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Judul Dashboard
st.title("🚴 Bike Sharing Data Dashboard")
st.markdown("Dashboard interaktif untuk menganalisis data penyewaan sepeda.")

# Load Data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('dashboard/day.csv')
        df['dteday'] = pd.to_datetime(df['dteday'])
        season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
        df['season'] = df['season'].map(season_map)
        return df
    except Exception as e:
        st.error(f"Error loading  {e}")
        return None

df = load_data()

if df is not None:
    # Sidebar Filter
    st.sidebar.header("Filter Data")
    selected_season = st.sidebar.multiselect(
        "Pilih Musim:",
        options=df['season'].unique(),
        default=df['season'].unique()
    )

    # Filter dataframe
    df_selected = df[df['season'].isin(selected_season)]

    # Metrik Utama
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Penyewaan", f"{df_selected['cnt'].sum():,}")
    with col2:
        st.metric("Rata-rata Harian", f"{df_selected['cnt'].mean():.0f}")
    with col3:
        st.metric("Total Casual User", f"{df_selected['casual'].sum():,}")

    st.divider()

    # Visualisasi 1
    st.subheader("1. Rata-Rata Penyewaan Berdasarkan Musim")
    fig1, ax1 = plt.subplots()
    sns.barplot(
        x='season', 
        y='cnt', 
        data=df_selected, 
        estimator=np.mean, 
        errorbar=None,  # ✅ Ganti ci=None dengan errorbar=None
        ax=ax1, 
        palette='viridis'
    )
    ax1.set_xlabel('Musim')
    ax1.set_ylabel('Rata-rata Penyewaan')
    st.pyplot(fig1)

    # Visualisasi 2
    st.subheader("2. Tren Penyewaan per Tanggal")
    fig2, ax2 = plt.subplots(figsize=(12, 5))
    sns.lineplot(x='dteday', y='cnt', data=df_selected, ax=ax2)
    ax2.set_xlabel('Tanggal')
    ax2.set_ylabel('Jumlah Penyewaan')
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    # Data Table
    with st.expander("Lihat Data Mentah"):
        st.dataframe(df_selected)
else:
    st.warning("Pastikan file 'day.csv' berada dalam folder yang sama dengan app.py")