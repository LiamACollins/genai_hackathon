import streamlit as st
from pages import walking_tour, user_preference_input  # Import the pages

# Main page
st.title('Welcome to the App')
st.write("This is the main page of the app. Click the button below to navigate to the user preference page.")

if st.button('Go to User Preferences'):
    # Update the session state to indicate navigation is requested
    st.switch_page("pages/user_preference_input.py")