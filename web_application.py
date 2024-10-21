# -*- coding: utf-8 -*-
"""Web application.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PQi8Kh9BR5NHyrd619LcMBkVyUUioYxl
"""

import streamlit as st
import numpy as np
import joblib


# Load the model
model = joblib.load('Randomforestmodel.pkl')


# Title for the web application
st.title('Bank Account Prediction')

st.write('Enter the following features to predict Bank account:')
country = st.selectbox('Country', ['Kenya', 'Uganda', 'Tanzania', 'Rwanda'])
location_type = st.radio('Location Type', ['Rural', 'Urban'])
cellphone_access = st.selectbox(' cellphone acessibility',['Yes','No'])
household_size = st.number_input('Household Size', min_value=1, max_value=50, value=1)
age_of_respondent = st.number_input('Age of Respondent', min_value=18, max_value=100, value=25)
gender_of_respondent = st.radio('Gender of Respondent', ['Male', 'Female'])
relationship_with_head = st.selectbox('Relationship with Head ', ['Head of household', 'Spouse', 'Child', 'Other relative','Parent'])
marital_status = st.selectbox('Marital Status', ['Married/Living together', 'Married', 'Divorced/separated', 'Widowed', 'Single/Never married'])
education_level = st.selectbox('Education Level', ['Secondary Education', 'Primary Education', 'No Formal Education', 'Vocational/Specialised Training'])
job_type = st.selectbox('Job Type', ['Dont know', 'Farming & Fishing', 'Formally Employed Government', 'Formally Employed Private', 'Government Dependent', 'Informally Employed', 'No Income', 'Other Income', 'Remittance Dependent', 'Self Employed'])

# Manually encode categorical variables
country_map = {'Kenya': 0, 'Uganda': 1, 'Tanzania': 2, 'Rwanda': 3}
cellphone_access_map = {'No': 0, 'Yes': 1}
location_type_map = {'Rural': 0, 'Urban': 1}
gender_map = {'Male': 0, 'Female': 1}
relationship_map = {'Head of household': 0, 'Spouse': 1, 'Child': 2, 'Other relative': 3, 'Parent': 4}
marital_status_map = {'Married/Living together': 0, 'Married': 1, 'Divorced/separated': 2, 'Widowed': 3, 'Single/Never married': 4}
education_map = {'Secondary Education': 0, 'Primary Education': 1, 'No Formal Education': 2, 'Vocational/Specialised Training': 3}
job_type_map = {
    'Dont know': 0, 'Farming & Fishing': 1, 'Formally Employed Government': 2,
    'Formally Employed Private': 3, 'Government Dependent': 4, 'Informally Employed': 5,
    'No Income': 6, 'Other Income': 7, 'Remittance Dependent': 8, 'Self Employed': 9
}

# Map the user inputs to numeric values
input_data = np.array([[country_map[country],
                        location_type_map[location_type],
                        cellphone_access_map[cellphone_access],
                        household_size,
                        age_of_respondent,
                        gender_map[gender_of_respondent],
                        relationship_map[relationship_with_head],
                        marital_status_map[marital_status],
                        education_map[education_level],
                        job_type_map[job_type]]])
# user input values
input_data = np.array([[country,
                        location_type,
                        cellphone_access,
                        household_size,
                        age_of_respondent,
                        gender_of_respondent,
                        relationship_with_head,
                        marital_status,
                        education_level,
                        job_type]])


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
