import streamlit as st
import pickle
import sklearn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier 

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Phishing Website Detector")

# Input fields
URLSimilarityIndex = st.number_input("URL Similarity Index", min_value=0.0, max_value=100.0, value=0.5)
LineOfCode = st.number_input("Number of Lines of Code", min_value=0, value=1000)
IsHTTPS = st.selectbox("Is HTTPS?", [0, 1])
LargestLineLength = st.number_input("Largest Line Length", min_value=0, value=1000)
NoOfExternalRef = st.number_input("Number of External References", min_value=0, value=5)

# Predict button
if st.button("Predict"):
    # Create DataFrame for model input
    input_data = pd.DataFrame([[URLSimilarityIndex, LineOfCode, IsHTTPS, LargestLineLength, NoOfExternalRef]],
                              columns=['URLSimilarityIndex', 'LineOfCode', 'IsHTTPS', 'LargestLineLength', 'NoOfExternalRef'])
    
    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    if prediction == 1:
        st.error("🚨 This is likely a phishing website!")
    else:
        st.success("✅ This is likely a safe website.")

