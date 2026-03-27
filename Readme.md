
# Cara Menjalankan Streamlit Menggunakan Virtual Environment (env)

## Langkah 1: Buat Virtual Environment

```bash
# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
venv\Scripts\activate
```

## Langkah 2: Install Package yang Diperlukan

```bash
# Install semua package dari requirements.txt
pip install -r requirements.txt

# Atau install satu per satu
pip install streamlit pandas matplotlib seaborn numpy
```
    
## Langkah 3: Jalankan Streamlit

```bash
# Pastikan virtual environment aktif (lihat ada (venv) di terminal)
# Kemudian jalankan:

streamlit run app.py
```
### 🌐 Dashboard akan terbuka otomatis di browser pada alamat: http://localhost:8501