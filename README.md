# 📰 Hoax News Detector - Klasifikasi Berita FAKE vs REAL

Aplikasi berbasis web untuk mendeteksi apakah sebuah berita tergolong **hoaks (FAKE)** atau **fakta (REAL)** menggunakan machine learning.

## 🔍 Fitur
- Input teks judul atau isi berita
- Klasifikasi otomatis: **FAKE** atau **REAL**
- Confidence Score (%)
- Dibangun dengan: Streamlit, Scikit-learn, TF-IDF

## 🧠 Dataset
- Sumber: [Fake and Real News Dataset - Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- Jumlah data: >40.000 (berita hoaks & fakta)

## 🚀 Cara Menjalankan Lokal

1. Clone repo ini:
    ```bash
    git clone https://github.com/username/hoax-news-detector.git
    cd hoax-news-detector
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Jalankan aplikasi:
    ```bash
    streamlit run app.py
    ```

## 🌐 Hosting Online

Deploy gratis menggunakan [Streamlit Cloud](https://streamlit.io/cloud) dengan menghubungkan repository ini ke akun Streamlit kamu.

## 📁 File Penting

- `model.pkl`: Model klasifikasi (Logistic Regression)
- `vectorizer.pkl`: TF-IDF Vectorizer
- `app.py`: Aplikasi web

## 📸 Screenshot
![screenshot](https://via.placeholder.com/800x400.png?text=Contoh+Tampilan+App+Streamlit)

---

Created with ❤️ by [Nama Kamu]
