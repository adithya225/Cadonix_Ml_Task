import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("best_model.pkl")

# Streamlit app
st.title("Customer Purchase Prediction")

# Input form
st.header("Enter Customer Details")
with st.form("prediction_form"):
    age = st.number_input("Age", min_value=0, max_value=100, value=25)
    country = st.selectbox("Country", ["India", "United States", "Germany", "UK"])
    pages_visited = st.number_input("Pages Visited", min_value=0, value=5)
    time_spent = st.number_input("Time Spent (minutes)", min_value=0, value=10)
    submit = st.form_submit_button("Predict")

# Preprocess inputs and make prediction
if submit:
    # Encode country
    country_mapping = {"India": "India", "United States": "united states", "Germany": "Germany", "UK": "UK"}
    country_encoded = country_mapping[country]

    # Create input DataFrame with correct column names
    input_data = pd.DataFrame([{
        "customer_id": "CUST20",  # Placeholder customer_id
        "age": age,
        "country": country_encoded,
        "pages_visited": pages_visited,
        "time_spent": time_spent
    }])
    st.write("Input Data:", input_data)

    # Make prediction
    prediction = model.predict(input_data)
    print(prediction)
    # Display result
    
    if prediction[0] == 1 and input_data["pages_visited"].iloc[0]!=0:
        if input_data["pages_visited"].iloc[0]!=0 and input_data["time_spent"].iloc[0]!=0:
            st.success("The customer is likely to make a purchase!")
        else:
            st.error("customer is visiting the page first time")
    else:
        st.error("The customer is unlikely to make a purchase.")