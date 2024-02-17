import streamlit as st
import time
import json

# Our first stop is Independence hall. In the end state this geolocation will be
# obtained through the javascript geolocation on the client

user_location = (39.949003945128936, -75.150088547482)
place = "Independence Hall, Philadelhpia"

with open('temp.json', 'r') as file:
    data = json.load(file)
    image_style = data['selected_image_option']

current_video = "geo_to_video/converted_hist_kodak_independence.mp4" if image_style == "Realistic old school photography shot on a kodak camera" else "geo_to_video/converted_thriller_vibrant_independence.mp4"
st.video(current_video, format="video/mp4", start_time=0)

time.sleep(18)
st.switch_page("pages/walking_tour_stop2.py")