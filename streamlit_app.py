import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Define the options for the dropdown
story_options = ['Historical facts', 'Political stories', 'Love stories', 'Mystery Thriller', 'Other']

# Display the multiselect dropdown
selected_options = st.multiselect('What kind of stories are you most interested in?', story_options)

# If the user selects "Other", prompt for text input
if 'Other' in selected_options:
    # Remove "Other" from the selected options temporarily
    selected_options.remove('Other')
    other_input = st.text_input('Specify what kind of stories you love:')
    # Append the input value to the selected options
    if other_input:
        selected_options.append(other_input)

# Concatenate the selected options into a single string
user_story_preference = ', '.join(selected_options)

# Image preferences
image_options = ['Realistic old school photography shot on a kodak camera',
                 'Vibrant and animated',
                 'Other']

# Display the dropdown
selected_option = st.selectbox('What kind of images do you want to see?', image_options)

# If the user selects "Other", prompt for text input
if selected_option == 'Other':
    other_input = st.text_input('Specify what kind of images you love:')
    if other_input:
        selected_option = other_input