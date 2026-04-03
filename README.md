![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)	![Google Colab](https://img.shields.io/badge/Google%20Colab-%23F9A825.svg?style=for-the-badge&logo=googlecolab&logoColor=white) ![image](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white))


# 🧠 Fetal Health Classification using Machine Learning

## 📌 Overview

Proyek ini bertujuan untuk mengklasifikasikan kondisi kesehatan janin (*fetal health*) menjadi tiga kategori:

* **Normal (1)**
* **Suspect (2)**
* **Pathological (3)**

Model machine learning dikembangkan untuk membantu proses analisis data medis berbasis fitur kardiotokografi (CTG), sehingga dapat mendukung pengambilan keputusan yang lebih akurat.

---

## 🎯 Objectives

* Membangun model klasifikasi multi-class
* Membandingkan performa beberapa algoritma machine learning
* Mengatasi permasalahan *class imbalance*
* Mengevaluasi model menggunakan metrik yang relevan (precision, recall, F1-score)

---

## 📊 Dataset

Dataset yang digunakan adalah **Fetal Health Dataset**, yang berisi berbagai fitur numerik hasil pengukuran CTG.

### 🔹 Target Variable

* `fetal_health`

  * 1 = Normal
  * 2 = Suspect
  * 3 = Pathological

---

## ⚙️ Methodology (CRISP-DM)

### 1. Business Understanding

Menentukan tujuan klasifikasi kondisi kesehatan janin.

### 2. Data Understanding

* Analisis distribusi data
* Deteksi *class imbalance*
* Visualisasi menggunakan:

  * Countplot
  * Heatmap korelasi

### 3. Data Preparation

* Train-test split (stratified)
* Penanganan *class imbalance* menggunakan **SMOTE**

### 4. Modeling

Model yang digunakan:

* 🌲 Random Forest
* 📈 Logistic Regression
* 📊 Naive Bayes
* 🔗 Ensemble (Voting Classifier)

### 5. Evaluation

Evaluasi model menggunakan:

* Confusion Matrix
* Classification Report:

  * Precision
  * Recall
  * F1-score

---

## 📈 Results & Analysis

* Dataset menunjukkan kondisi **imbalanced**, di mana kelas *Normal* mendominasi.
* Setelah penerapan **SMOTE**, distribusi data menjadi lebih seimbang.
* Model **Random Forest** memberikan performa terbaik dibandingkan model lainnya.
* Ensemble tidak selalu meningkatkan performa, tergantung pada kombinasi model.

---

## 🧪 Key Insights

* Akurasi bukan satu-satunya metrik yang penting, terutama pada dataset medis.
* Recall pada kelas minoritas (Suspect & Pathological) menjadi fokus utama.
* SMOTE membantu meningkatkan kemampuan model dalam mengenali kelas minoritas.

---

## 🏆 Best Model

**Random Forest** dipilih sebagai model terbaik karena:

* Performa stabil di semua kelas
* Nilai F1-score tinggi
* Mampu menangani data non-linear dengan baik

---

## 📌 Feature Importance

Analisis menunjukkan bahwa beberapa fitur memiliki kontribusi signifikan terhadap klasifikasi kondisi janin, yang dapat digunakan sebagai indikator penting dalam analisis medis.

---

## 🚀 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Imbalanced-learn (SMOTE)
* Matplotlib, Seaborn

---

## 📂 Project Structure

```
├── fetal_health.csv
├── notebook.ipynb
├── README.md
```

---

## ▶️ How to Run

1. Clone repository:

```bash
git clone https://github.com/username/fetal-health-classification.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run notebook:

```bash
jupyter notebook
```

---

## 📚 Conclusion

Pendekatan machine learning dengan penanganan *class imbalance* terbukti mampu meningkatkan kualitas klasifikasi pada dataset medis. Model Random Forest memberikan performa terbaik dan dapat dijadikan baseline untuk pengembangan lebih lanjut.

---

## ✨ Future Work

* Hyperparameter tuning
* Cross-validation
* Deployment (API / Web App)
* Explainable AI (SHAP / LIME)

---

## 👤 Author

**Ananda Ahmad Fadhillah**
Information Systems Student – Telkom University

---
