import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("academic_warning_model.pkl", "rb"))

st.title("Academic Warning Prediction")

st.write("Nhập thông tin sinh viên:")

age = st.number_input("Age", 17, 40, 20)
tuition_debt = st.number_input("Tuition Debt", 0.0, 10000000.0, 0.0)
count_f = st.number_input("Number of F grades", 0, 20, 0)
training_score = st.number_input("Training Score", 0.0, 100.0, 70.0)

if st.button("Predict"):

    features = np.array([[age, tuition_debt, count_f, training_score]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Student at Academic Risk")
    else:
        st.success("✅ Student is Safe")
