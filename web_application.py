# -*- coding: utf-8 -*-
"""Web application.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PQi8Kh9BR5NHyrd619LcMBkVyUUioYxl
"""

import streamlit as st
import numpy as np
import pickle
import joblib

# Load the model
model = joblib.load('Financialmodel.pkl')

# Load the encoders
with open('label_encoders.pkl', 'rb') as file:
    label_encoders = pickle.load(file)

# Title for the web application
st.title('Bank Account Prediction')

st.write('Enter the following features to predict Bank account:')
country = st.selectbox('Country', ['Kenya', 'Uganda', 'Tanzania', 'Rwanda'])
location_type = st.radio('Location Type', ['Rural', 'Urban'])
cellphone_access = st.selectbox('Cellphone Accessibility', ['Yes', 'No'])
household_size = st.number_input('Household Size', min_value=1, max_value=50, value=1)
age_of_respondent = st.number_input('Age of Respondent', min_value=18, max_value=100, value=25)
gender_of_respondent = st.radio('Gender of Respondent', ['Male', 'Female'])
relationship_with_head = st.selectbox('Relationship with Head', ['Head of Household', 'Spouse', 'Child', 'Other relative', 'Parent'])
marital_status = st.selectbox('Marital Status', ['Married/Living together', 'Married', 'Divorced/separated', 'Widowed', 'Single/Never married'])
education_level = st.selectbox('Education Level', ['Secondary education', 'Primary education', 'No formal education', 'Vocational/Specialised Training'])
job_type = st.selectbox('Job Type', ['Dont Know/Refuse to answer', 'Farming & Fishing', 'Formally employed Government', 'Formally employed Private', 'Government Dependent', 'Informally employed', 'No Income', 'Other Income', 'Remittance Dependent', 'Self employed'])

# Map user inputs to numeric values using the loaded encoders
input_data = np.array([[label_encoders['country'].transform([country])[0],
                        label_encoders['location_type'].transform([location_type])[0],
                        label_encoders['cellphone_access'].transform([cellphone_access])[0],
                        household_size,
                        age_of_respondent,
                        label_encoders['gender_of_respondent'].transform([gender_of_respondent])[0],
                        label_encoders['relationship_with_head'].transform([relationship_with_head])[0],
                        label_encoders['marital_status'].transform([marital_status])[0],
                        label_encoders['education_level'].transform([education_level])[0],
                        label_encoders['job_type'].transform([job_type])[0]]])

# Create a dictionary for the prediction labels
prediction_labels = {0: 'No Bank Account', 1: 'Bank Account'}

# Prediction button
if st.button('Predict'):
    # Make prediction using the loaded model
    prediction = model.predict(input_data)

    # Convert numeric prediction to corresponding string label
    prediction_result = prediction_labels.get(prediction[0], "Unknown")


    # Display the prediction result
    st.write(f'Predicted outcome: {prediction_result}')

