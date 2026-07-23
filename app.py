import streamlit as st

st.set_page_config(page_title="Car Price Prediction", layout="centered")

st.markdown("""
<style>
    .stApp {background-color: #0E1117; color: white;}
    h1 {color: white;}
</style>
""", unsafe_allow_html=True)

st.title("Car Price Prediction App")

model = st.selectbox("Model", ["Fiesta", "Focus", "EcoSport", "Endeavour"])
year = st.number_input("Year", min_value=2000, max_value=2026, value=2020)
mileage = st.number_input("Mileage", min_value=0, value=50000)
tax = st.number_input("Tax", min_value=0, value=150)
mpg = st.number_input("MPG", min_value=0.0, value=50.00)
engine_size = st.number_input("Engine Size", min_value=0.5, value=1.50)
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Hybrid"])

if st.button("Predict Price"):
    predicted_price = 8500
    st.success(f"Predicted Car Price: $ {predicted_price}")
