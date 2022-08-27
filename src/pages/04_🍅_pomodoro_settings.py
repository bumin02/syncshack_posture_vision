import streamlit as st

st.title("Pomodoro settings")

n_cycle = st.number_input("How many pomodory cycle are you planning to do today? ",value=3, format="%i")
st.text(f"You will do {n_cycle} today")

work_interval = st.slider("How long would you like to work: ", 
                        20,120, 45)
st.text(f"You will work for {work_interval} minutes for each pomodoro cycle")

rest_interval = st.slider("How long would you like to rest: ",
                        5,60,5)
st.text(f"You will rest for {rest_interval} minutes for each pomodoro cycle")
