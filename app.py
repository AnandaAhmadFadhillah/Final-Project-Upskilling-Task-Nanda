import streamlit as st
import pandas as pd
import pickle

# Memuat model
try:
    with open('trained_model.sav', 'rb') as file:
        loaded_model = pickle.load(file)
except FileNotFoundError:
    st.error("Error: 'trained_model.sav' tidak ditemukan. Pastikan file model berada di direktori yang sama.")
    st.stop()

# Fitur-fitur yang digunakan (21 fitur)
selected_features = ['baseline value', 'accelerations', 'fetal_movement', 'uterine_contractions', 'light_decelerations', 'severe_decelerations', 'prolongued_decelerations', 'abnormal_short_term_variability', 'mean_value_of_short_term_variability', 'percentage_of_time_with_abnormal_long_term_variability', 'mean_value_of_long_term_variability', 'histogram_width', 'histogram_min', 'histogram_max', 'histogram_number_of_peaks', 'histogram_number_of_zeroes', 'histogram_mode', 'histogram_mean', 'histogram_median', 'histogram_variance', 'histogram_tendency']

# Fungsi prediksi kesehatan janin
def predict_fetal_health_full(input_values):
    if len(input_values) != len(selected_features):
        raise ValueError(f"Diharapkan {len(selected_features)} nilai input, tetapi mendapat {len(input_values)}.")

    input_df = pd.DataFrame([input_values], columns=selected_features)
    prediction = loaded_model.predict(input_df)

    def map_prediction_to_label(pred_value):
        if pred_value == 1.0:
            return "Normal"
        elif pred_value == 2.0:
            return "Suspect"
        elif pred_value == 3.0:
            return "Pathological"
        else:
            return "Unknown"

    predicted_label = map_prediction_to_label(prediction[0])
    return predicted_label, int(prediction[0])

# --- Antarmuka Streamlit ---
st.title("Prediksi Kondisi Kesehatan Janin")
st.write("Aplikasi ini memprediksi kondisi kesehatan janin (Normal, Suspect, Pathological) berdasarkan 21 fitur.")

# Input pengguna
input_values = []
for i, feature_name in enumerate(selected_features):
    value = st.number_input(f"{feature_name} ({i+1}/{len(selected_features)}):", value=0.0, step=0.001)
    input_values.append(value)

if st.button("Prediksi Kesehatan Janin"):
    try:
        predicted_label, predicted_class = predict_fetal_health_full(input_values)
        st.success(f"Prediksi Status Kesehatan Janin: **{predicted_label}** (Kelas: **{predicted_class}**)")
    except ValueError as e:
        st.error(f"Error: {e}")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")
