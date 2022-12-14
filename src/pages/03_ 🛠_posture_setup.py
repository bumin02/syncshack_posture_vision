import streamlit as st
import cv2
import numpy as np
from posture_tracker import benchmark_photo

st.title("Posture settings")

help_msg = '''
    For the best result, show your head and both shoulders clearly.
        '''
img_file_buffer = st.camera_input("Set benchmark posture", help=help_msg)

if img_file_buffer:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    cv2_img = benchmark_photo(cv2_img)
    st.write(cv2_img.shape)
    st.image(cv2_img)

