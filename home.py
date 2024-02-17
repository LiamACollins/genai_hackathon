import streamlit as st
from pages import user_preference_input, walking_tour_stop1  # Import the pages

st.set_page_config(
   page_title="Ex-stream-ly Cool App",
   page_icon="🧊",
   layout="centered",
   initial_sidebar_state="collapsed",
)

# Main page
# Use columns to center the "Next" button
col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button('Next'):
        st.switch_page("pages/user_preference_input.py")

st.image("assets/images/Philadelphia_landmark_landing.webp")