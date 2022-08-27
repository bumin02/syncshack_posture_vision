import streamlit as st

if 'running' not in st.session_state:
    st.session_state.running = False

def toggle():
    st.session_state.running = not st.session_state.running

st.image("./spine_logo.png")
st.markdown(
'''
    ### Welcome to.... (DESCRIPTION NEEDED)
''')

st.markdown("<h1 style='text-align: center;'>Spine is running...</h1>" if st.session_state.running else
            "<h1 style='text-align: center;'>Click start to run Spine</h1>", unsafe_allow_html=True)
_, mid, _ = st.columns([11,10,4])
mid.button("START" if not st.session_state.running else "STOP", on_click=toggle)
