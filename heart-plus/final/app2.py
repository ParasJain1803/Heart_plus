import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('heart_disease_model.pkl')

# Set page config for a more professional layout
st.set_page_config(page_title="Heart+ (Smart Heart Care)", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #FFF4B7;
        }
        h1 {
            text-align: center;
            color: #000B58;
            font-size: 42px;
            margin: 20px 0;
            animation: fadeIn 1s ease-in;
        }
        .card {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin: 20px 0;
            transition: transform 0.2s;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
        }
        .button {
            background-color: #006A67;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        .button:hover {
            background-color: #003161;
        }
        .prediction {
            text-align: center;
            font-size: 36px;
            animation: fadeIn 1s ease-in;
        }
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit app title
st.markdown("<h1>Heart+ (Smart Heart Care)</h1>", unsafe_allow_html=True)

# Create a container for the user input form
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    # Collect user inputs
    age = st.number_input('Age', min_value=1, max_value=120, value=25)
    sex = st.selectbox('Sex', options=['M', 'F'], format_func=lambda x: 'Male' if x == 'M' else 'Female')
    chest_pain = st.selectbox('Chest Pain Type', options=['TA', 'ATA', 'NAP', 'ASY'], format_func=lambda x: {
        'TA': 'Typical Angina', 'ATA': 'Atypical Angina', 'NAP': 'Non-Anginal Pain', 'ASY': 'Asymptomatic'
    }[x])
    resting_bp = st.number_input('Resting Blood Pressure (mm Hg)', min_value=80, max_value=200, value=120)
    cholesterol = st.number_input('Cholesterol (mg/dL)', min_value=100, max_value=400, value=200)
    fasting_bs = st.selectbox('Fasting Blood Sugar > 120 mg/dL', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    resting_ecg = st.selectbox('Resting ECG', options=['Normal', 'ST', 'LVH'], format_func=lambda x: {
        'Normal': 'Normal', 'ST': 'ST-T wave abnormality', 'LVH': 'Left ventricular hypertrophy'
    }[x])
    max_hr = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
    exercise_angina = st.selectbox('Exercise Induced Angina', options=['Y', 'N'], format_func=lambda x: 'Yes' if x == 'Y' else 'No')
    oldpeak = st.number_input('Oldpeak (ST depression)', min_value=0.0, max_value=10.0, value=1.0)
    st_slope = st.selectbox('ST Slope', options=['Up', 'Flat', 'Down'])
    
    st.markdown("</div>", unsafe_allow_html=True)  # Close the input form card
    
    # Prediction button
    if st.button('Predict', key='predict_button', help='Click to predict heart disease risk', css_class='button'):
        # Create a DataFrame from user input
        input_data = pd.DataFrame({
            'Age': [age],
            'Sex': [sex],
            'ChestPainType': [chest_pain],
            'RestingBP': [resting_bp],
            'Cholesterol': [cholesterol],
            'FastingBS': [fasting_bs],
            'RestingECG': [resting_ecg],
            'MaxHR': [max_hr],
            'ExerciseAngina': [exercise_angina],
            'Oldpeak': [oldpeak],
            'ST_Slope': [st_slope]
        })

        # Predict using the model
        prediction = model.predict(input_data)[0]

        # Display the result
        if prediction == 1:
            st.markdown("<h2 class='prediction' style='color: red;'>Prediction: Positive for Heart Disease</h2>", unsafe_allow_html=True)
        else:
            st.markdown("<h2 class='prediction' style='color: green;'>Prediction: Negative for Heart Disease</h2>", unsafe_allow_html=True)
