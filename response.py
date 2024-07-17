import streamlit as st

def get_app_response(prediction):
  if prediction == 1: # CHANGE THIS!
    st.write("The model predicts that you have a heart disease")
  # ADD MORE IF / ELIF STATEMENTS HERE
  else:
    st.write("The model predicts that you don't have a heart disease")
