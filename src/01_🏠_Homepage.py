import streamlit as st
import os
import subprocess

if 'running' not in st.session_state:
    st.session_state.running = False

def toggle():
    st.session_state.running = not st.session_state.running
    subprocess.Popen(["python3", "posture_tracker.py"])


st.image("./spine_logo.png")
st.markdown(
'''
    ### Welcome to Spine!
    1. Go to "posture setup"
    2. Sit upright in your best posture and click "Take Photo"!
    3. Come back to the Homepage and click Start!
    4. How your posture will be tracked throughout your session :)
''')

st.markdown("<h1 style='text-align: center;'>Spine is running...</h1>" if st.session_state.running else
            "<h1 style='text-align: center;'>Click start to run Spine</h1>", unsafe_allow_html=True)
_, mid, _ = st.columns([11,10,4])
mid.button("START" if not st.session_state.running else "STOP", on_click=toggle)
