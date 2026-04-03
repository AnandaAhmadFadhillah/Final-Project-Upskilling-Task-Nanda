![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)	![Google Colab](https://img.shields.io/badge/Google%20Colab-%23F9A825.svg?style=for-the-badge&logo=googlecolab&logoColor=white) ![image](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)


# 🧠 Prediksi Kondisi Kesehatan Janin Menggunakan Random Forest

## 📌 Deskripsi Proyek

Proyek ini merupakan implementasi *machine learning* untuk memprediksi kondisi kesehatan janin berdasarkan data *Cardiotocography (CTG)*. Model yang digunakan adalah **Random Forest Classifier**, yang dipilih karena kemampuannya dalam menangani data kompleks serta menghasilkan performa klasifikasi yang stabil.

Aplikasi ini dikembangkan menggunakan **Streamlit** sehingga dapat digunakan secara interaktif melalui web interface.

---

## 🎯 Tujuan

* Mengklasifikasikan kondisi kesehatan janin ke dalam 3 kategori:

  * **Normal**
  * **Suspect**
  * **Pathological**
* Membantu memberikan *decision support* awal dalam analisis kesehatan janin

---

## 📊 Dataset

Dataset yang digunakan adalah data *Fetal Health* yang terdiri dari:

* 21 fitur numerik hasil pengukuran CTG
* Label target berupa kondisi kesehatan janin

Contoh fitur:

* Baseline value
* Accelerations
* Fetal movement
* Uterine contractions
* Decelerations (light, severe, prolonged)

---

## ⚙️ Metodologi

### 1. Preprocessing

* Data cleaning
* Handling missing values (jika ada)
* Penanganan *imbalanced data* menggunakan **SMOTE**

### 2. Model yang Digunakan

Model utama:

* 🌳 **Random Forest Classifier**

Alasan pemilihan:

* Mampu menangani non-linear relationship
* Robust terhadap overfitting
* Memberikan *feature importance* untuk interpretasi

---

## 📈 Evaluasi Model

Model dievaluasi menggunakan:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

Random Forest dipilih sebagai model terbaik berdasarkan performa evaluasi dibandingkan:

* Logistic Regression
* Naive Bayes
* Ensemble Model

---

## 🚀 Deployment

Aplikasi di-deploy menggunakan:

* **Streamlit** (frontend & backend)
* Dapat dijalankan secara lokal atau melalui tunneling (LocalTunnel / Ngrok)

---

## 💻 Cara Menjalankan Aplikasi

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Jalankan aplikasi

```bash
python -m streamlit run app.py
```

### 3. Akses di browser

```
http://localhost:8501
```

---

## 🖥️ Tampilan Aplikasi

Aplikasi menyediakan:

* Input 21 fitur numerik
* Tombol prediksi
* Output berupa:

  * Label kondisi kesehatan janin
  * Kelas prediksi

---

## 🧠 Insight Model

Random Forest memungkinkan analisis terhadap fitur yang paling berpengaruh dalam menentukan kondisi janin, sehingga tidak hanya memberikan prediksi, tetapi juga mendukung interpretasi medis secara awal.

---

## ⚠️ Keterbatasan

* Dataset tidak berasal dari data klinis real-time
* Model belum diuji pada lingkungan medis sebenarnya
* Interpretasi masih bersifat *decision support*, bukan diagnosis final

---

## 🔮 Pengembangan Selanjutnya

* Integrasi dengan sistem rumah sakit
* Penambahan data real-time
* Eksperimen dengan model lain (XGBoost, Deep Learning)
* Visualisasi feature importance di aplikasi

---

## 👨‍💻 Author

Ananda Ahmad Fadhillah
S1 Sistem Informasi – Telkom University

---

## 📌 Catatan

Aplikasi ini dibuat untuk tujuan akademik dan penelitian, bukan sebagai pengganti diagnosis medis profesional.
