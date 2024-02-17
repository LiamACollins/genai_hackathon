import streamlit as st
import json

st.title("You've arrived!")

# Open variables in temp file
with open('temp.json', 'r') as file:
    data = json.load(file)
    image_style = data['selected_image_option']

# Display generated video
current_video = "geo_to_video/converted_hist_kodak_bell.mp4" if image_style == "Realistic old school photography shot on a kodak camera" else "geo_to_video/converted_thriller_vibrant_bell.mp4"
st.video(current_video, format="video/mp4", start_time=0)