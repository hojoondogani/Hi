import streamlit as st

def get_user_input():
  age = st.number_input("What is your age?")
  blood_pressure = st.number_input("What is your blood pressure?")
  chloseterol = st.number_input("What is your cholesterol?")
  heart_rate = st.number_input("What is your maximum heart rate")
  sex = st.number_input("What is your sex?")
  high_blood_sugar = st.number_input("Do you have high blood sugar?")
  chest_pain = st.number_input("Do you have chest pain?")
  exercise_pain = st.number_input("Do you have exercise pain?")
  input_features = [[blood_pressure, heart_rate]] # put your features in here!
  return input_features
