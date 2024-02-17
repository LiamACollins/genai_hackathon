import streamlit as st

# Our first stop is Independence hall. In the end state this geolocation will be
# obtained through the javascript geolocation on the client

user_location = (39.949003945128936, -75.150088547482)
place = "Independence Hall, Philadelhpia"

# TODO: Call create image to get the Base10 generated image

st.image("assets/images/Independence Hall Kodak Style.webp",
         caption=place)