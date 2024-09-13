import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the trained model and scaler
with open('heart_disease_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Function to make predictions
def predict_heart_disease(input_data):
    input_data = scaler.transform(np.array(input_data).reshape(1, -1))
    prediction = model.predict(input_data)
    return prediction

# Streamlit app layout
def main():
    st.title("Heart +")

    # Collect user inputs
    age = st.slider('Age', 20, 100, 50)
    sex = st.selectbox('Sex', ['Male', 'Female'])
    chest_pain_type = st.selectbox('Chest Pain Type', ['ATA', 'NAP', 'ASY', 'TA'])
    resting_bp = st.number_input('Resting Blood Pressure', 80, 200, 120)
    cholesterol = st.number_input('Cholesterol Level', 100, 400, 200)
    fasting_blood_sugar = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'])
    resting_ecg = st.selectbox('Resting ECG results', ['Normal', 'ST', 'LVH'])
    max_hr = st.slider('Maximum Heart Rate Achieved', 60, 220, 150)
    exercise_angina = st.selectbox('Exercise-Induced Angina', ['Yes', 'No'])
    oldpeak = st.number_input('Oldpeak (ST depression induced by exercise)', 0.0, 10.0, 1.0)
    st_slope = st.selectbox('ST Slope', ['Up', 'Flat', 'Down'])

    # Convert user inputs into model-ready format
    sex = 1 if sex == 'Male' else 0
    chest_pain_type = {'ATA': 0, 'NAP': 1, 'ASY': 2, 'TA': 3}[chest_pain_type]
    fasting_blood_sugar = 1 if fasting_blood_sugar == 'Yes' else 0
    resting_ecg = {'Normal': 0, 'ST': 1, 'LVH': 2}[resting_ecg]
    exercise_angina = 1 if exercise_angina == 'Yes' else 0
    st_slope = {'Up': 0, 'Flat': 1, 'Down': 2}[st_slope]

    # Create a feature list for prediction
    input_data = [age, sex, chest_pain_type, resting_bp, cholesterol, fasting_blood_sugar,
                  resting_ecg, max_hr, exercise_angina, oldpeak, st_slope]

    # Display a button for prediction
    if st.button('Predict'):
        prediction = predict_heart_disease(input_data)
        if prediction == 1:
            st.error("Warning! You have a high risk of heart disease.")
        else:
            st.success("You are at low risk of heart disease.")

# Run the Streamlit app
if __name__ == '__main__':
    main()
