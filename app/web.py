import os
import pickle as pkl
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config("PREDICT DISEASE OUTBREAKS",
                   layout="wide",
                   page_icon="doctor")

try:
    diabeties_model = pkl.load(open("model_sets/diabeties_model.pkl", "rb"))
    heart_disease_model = pkl.load(open("model_sets/heart_disease_model.pkl", "rb"))
    parkinsons_model = pkl.load(open("model_sets/parkinsons_model.pkl", "rb"))
except Exception as e:
    st.error("Error loading models. Please check the file paths and ensure the models exist.")
    st.stop()

with st.sidebar:
    selected = option_menu("Prediction of Disease Outbreak", ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"],
                           menu_icon="hospital-fill", icons=["activity", "heart", "person"], default_index=0)

if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction Using ML")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("No. of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    with col2:
        Age = st.text_input("Age")

    if st.button("Diabetes Test Result"):
        try:
            user_input = [float(x) for x in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
            prediction = diabeties_model.predict([user_input])
            st.success("The person is Diabetic" if prediction[0] == 1 else "The person is not Diabetic")
        except Exception as e:
            st.error("Error in prediction. Please check your inputs.")

if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction Using ML")
    cols = st.columns(4)
    labels = ["Age", "Gender", "Chest Pain types", "Resting Blood Pressure", "Serum Cholesterol in mg/dl", 
              "Fasting Blood Sugar > 120 mg/dl", "Resting Electrocardiographic results", "Maximum Heart Rate Achieved", 
              "Exercise Induced Angina", "ST Depression Induced by Exercise", "Slope of the Peak Exercise ST Segment", 
              "Major Vessels Colored by Fluoroscopy", "Thal"]
    inputs = [cols[i % 4].text_input(labels[i]) for i in range(len(labels))]
    
    if st.button("Heart Test Result"):
        try:
            user_input = [float(x) for x in inputs]
            prediction = heart_disease_model.predict([user_input])
            st.success("The person has Heart Disease" if prediction[0] == 1 else "The person does not have Heart Disease")
        except Exception as e:
            st.error("Error in prediction. Please check your inputs.")

if selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    labels = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP', 
              'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5', 
              'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE']
    
    cols = st.columns(5)
    inputs = [cols[i % 5].text_input(label) for i, label in enumerate(labels)]

    if st.button("Parkinson's Test Result"):
        try:
            user_input = [float(x) for x in inputs]
            prediction = parkinsons_model.predict([user_input])
            st.success("The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease")
        except Exception as e:
            st.error("Error in prediction. Please check your inputs.")
