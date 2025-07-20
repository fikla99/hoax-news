import streamlit as st
import pickle
import numpy as np

# Load model dan vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Tampilan aplikasi
st.set_page_config(page_title="Klasifikasi Berita Hoaks vs Fakta")
st.title("📰 Deteksi Berita Hoaks")
st.markdown("Masukkan **judul atau ringkasan berita**, dan sistem akan memprediksi apakah berita tersebut FAKE atau REAL.")

# Input dari pengguna
input_text = st.text_area("Masukkan teks berita di sini:", height=150)

# Tombol prediksi
if st.button("Prediksi"):
    if input_text.strip() == "":
        st.warning("Silakan masukkan teks terlebih dahulu.")
    else:
        # Transformasi dan prediksi
        input_vec = vectorizer.transform([input_text])
        prediction = model.predict(input_vec)[0]
        probas = model.predict_proba(input_vec)[0]

        # Tampilkan hasil
        st.subheader("Hasil Prediksi:")
        if prediction == "FAKE":
            st.error(f"❌ Prediksi: **{prediction}** (Hoaks)")
        else:
            st.success(f"✅ Prediksi: **{prediction}** (Fakta)")

        # Tampilkan confidence score
        st.markdown(f"**Confidence:** {np.max(probas)*100:.2f}%")
