
## Langkah 1: Buat Virtual Environment

Windows:

```bash
# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
venv\Scripts\activate
```

Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
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

# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Pastikan berada di folder streamlit
cd dashboard
# Kemudian jalankan:

streamlit run app.py
```
### 🌐 Dashboard akan terbuka otomatis di browser pada alamat: http://localhost:8501