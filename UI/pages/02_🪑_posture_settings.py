import streamlit as st

st.title("Posture settings")

st.subheader("Posture detections settings")
st.slider("How much percentage change in shoulder to shoulder distance should be consider slouching: ", 0,100,5)
st.slider("How much percentage change in distance from head to neck base should be consider slouching: ", 0, 100 , 25)
st.slider("What is minimum amount of head tilt should be considered slouching: ", 0, 90,30)

st.subheader("Technical settings")
tracking_interval = st.slider("How many times per minute do you want the program to scan your posture: ", 1, 60, 12)

st.sidebar.title("🪑 Posture settings")