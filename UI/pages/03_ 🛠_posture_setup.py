import streamlit as st
from urfolder import yourfile
import cv2

st.title("Posture settings")

help_msg = '''
    For the best result, show your head and both shoulders clearly.
        '''
picture = st.camera_input("Set benchmark posture", help=help_msg)

if picture:
    st.image(picture)

st.sidebar.title("🛠 Posture setup")