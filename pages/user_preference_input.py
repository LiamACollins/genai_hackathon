import streamlit as st
import json

# Define the options for the dropdown
story_options = ['Historical facts', 'Political stories', 'Love stories', 'Mystery Thriller', 'Other']

# Display the multiselect dropdown
selected_story_options = st.multiselect('What kind of stories are you most interested in?', story_options)

# If the user selects "Other", prompt for text input
if 'Other' in selected_story_options:
    other_input = st.text_input('Specify what kind of stories you love:')
    # Append the input value to the selected options
    if other_input:
        selected_story_options.append(other_input)

# Concatenate the selected options into a single string
user_story_preference = ', '.join(selected_story_options)

# Image preferences
image_options = ['Realistic old school photography shot on a kodak camera',
                 'Vibrant and animated',
                 'Other']

# Display the dropdown
selected_image_option = st.selectbox('What kind of images do you want to see?', image_options)

# If the user selects "Other", prompt for text input
if selected_image_option == 'Other':
    other_input = st.text_input('Specify what kind of images you love:')
    if other_input:
        selected_image_option = other_input

# Dump variables to temp JSON file to be used by other scripts
data = {'selected_story_type': user_story_preference,
        'selected_image_option': selected_image_option}
with open('temp.json', 'w') as file:
    json.dump(data, file)

if st.button('Submit'):
    st.switch_page("pages/walking_tour_stop1.py")