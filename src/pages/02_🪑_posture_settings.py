import streamlit as st
import csv
import os

def saveChange():
    global s2s, h2n, ht, slouch_max
    with open("./.settings", "w") as f:
        f.write(f"{s2s}\n{h2n}\n{ht}\n{slouch_max}")

def reset():
    os.system("cp ./.basesettings ./.settings")

with open("./.settings", "r") as f:
    settings = f.readlines()
    s2s =  int(settings[0])
    h2n = int(settings[1])
    ht = int(settings[2])
    slouch_max = int(settings[3])

st.title("Posture settings")

st.subheader("Posture detections settings")
s2s = st.slider("How much percentage change in shoulder to shoulder distance should be consider slouching: ", 0,100,s2s)
h2n = st.slider("How much percentage change in distance from head to neck base should be consider slouching: ", 0, 100 , h2n)
ht = st.slider("What is minimum amount of head tilt should be considered slouching: ", 0, 90,ht)

st.subheader("Technical settings")
slouch_max = st.slider("How many seconds after you slouch should we alert you: ", 1, 120, slouch_max)

b1, b2, _ = st.columns([1,1,8])
b1.button("Apply!", on_click=saveChange)
b2.button("Reset!", on_click=reset)
    