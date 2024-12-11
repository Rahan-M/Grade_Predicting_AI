import streamlit as st
import pandas as pd
import numpy as np
import joblib

model=joblib.load("grade_prediction_ai.pkl")
def convert(s):
    if s=="Very Bad" :
        return 1
    elif s=="Bad" :
        return 2
    elif s=="Okay" :
        return 3
    elif s=="Good" :
        return 4
    elif s=="Excellent" :
        return 5


st.title("Grade Prediction AI")

# iii absences - number of school absences (numeric: from 0 to 93)
# v age - student's age (numeric: from 15 to 22)
# iv famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
# ii G1 - first period grade (numeric: from 0 to 20)
# i G2 - second period grade (numeric: from 0 to 20)
options=['Very Bad','Bad','Okay','Good','Excellent']
with st.form(key='student_detaiils'):
    absences = st.number_input('How many leaves did you take? (0-93)', min_value=0, max_value=93, value=0)
    age = st.number_input('Enter your age (15-22)', min_value=15, max_value=22, value=17)
    famrel=st.selectbox("Rate the quality of your family relationships",options)
    G1 = st.number_input('Enter your first period grade (0-20)', min_value=0, max_value=20, value=14)
    G2 = st.number_input('Enter your second period grade (0-20)', min_value=0, max_value=20, value=14)

    submit_button=st.form_submit_button(label="Predict Grade")

if submit_button:
    famrel_n=convert(famrel)
    feature_names=['absences','age','famrel','G1','G2']
    input_data=pd.DataFrame([[absences,age,famrel_n,G1,G2]], columns=feature_names) #Created this to remove a warning, Works fine even if you directly input the 2D-array
    prediction=model.predict(input_data)
    st.write(f"Predicted Grade = {prediction[0]:.2f}")



