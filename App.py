
# Heart Disease Prediction Web App
# Using Library: 
import streamlit as st
import pandas as pd
import joblib 

# Load the model, scaler, and expected columns
model = joblib.load('KNN_heart.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns_data = joblib.load('columns.pkl')

# Check if expected_columns_data is a method and call it if needed
if callable(expected_columns_data):
    expected_columns = expected_columns_data()
else:
    expected_columns = expected_columns_data

# Make sure expected_columns is iterable (a list)
if not hasattr(expected_columns, '__iter__') or isinstance(expected_columns, str):
    st.error("Error: Expected columns format is invalid. Please check your columns.pkl file.")
    st.stop()

# Title and description of the web app
st.title('Heart Stroke Prediction by Shanku💖')
st.markdown("Provide the following details")

# Columns used during model training excluding the target variable
age = st.slider("Age", 18, 100, 40)
sex = st.selectbox('Sex', ['Male', 'Female'])
chest_pain = st.selectbox('Chest Pain Type', ['ATA', 'NAP', 'TA', 'ASY'])
resting_bp = st.number_input('RestingBP (mm Hg)', 80, 200, 120)
cholesterol = st.number_input('Cholesterol (mg/dL)', 100, 600, 200)
fasting_bs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])
resting_ecg = st.selectbox('Resting ECG', ['Normal', 'ST', 'LVH'])
max_hr = st.slider('Max Heart Rate', 60, 220, 150)
exercise_angina = st.selectbox('Exercise-Induced Angina', ['Yes', 'No'])
oldpeak = st.slider('Oldpeak (ST Depression)', 0.0, 6.0, 1.0) 
st_slope = st.selectbox('ST Slope', ['Up', 'Flat', 'Down'])

if st.button('Predict'):

    st.balloons()
    # Create a dictionary with all the input values
    input_dict = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_Female': 1 if sex == 'Female' else 0,
        'Sex_Male': 1 if sex == 'Male' else 0,
        'ChestPainType_ATA': 1 if chest_pain == 'ATA' else 0,
        'ChestPainType_NAP': 1 if chest_pain == 'NAP' else 0,
        'ChestPainType_TA': 1 if chest_pain == 'TA' else 0,
        'ChestPainType_ASY': 1 if chest_pain == 'ASY' else 0,
        'RestingECG_LVH': 1 if resting_ecg == 'LVH' else 0,
        'RestingECG_Normal': 1 if resting_ecg == 'Normal' else 0,
        'RestingECG_ST': 1 if resting_ecg == 'ST' else 0,
        'ExerciseAngina_No': 1 if exercise_angina == 'No' else 0,
        'ExerciseAngina_Yes': 1 if exercise_angina == 'Yes' else 0,
        'ST_Slope_Down': 1 if st_slope == 'Down' else 0,
        'ST_Slope_Flat': 1 if st_slope == 'Flat' else 0,
        'ST_Slope_Up': 1 if st_slope == 'Up' else 0
    }
    
    # Create a DataFrame with the input data
    input_df = pd.DataFrame([input_dict])
    
    # Debug: Show what columns we have and what's expected
    st.write("Input columns:", list(input_df.columns))
    st.write("Expected columns:", expected_columns)
    
    # Ensure all expected columns are present (fill missing with 0)
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    
    # Reorder the columns to match the training data
    input_df = input_df[expected_columns]
    
    # Scaling the input data and making prediction
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)
    
    # Display the prediction result
    if prediction[0] == 1:
        st.error("❌ High Risk of Heart Disease")
    else:
        st.success('✅ Low Risk of Heart Disease')