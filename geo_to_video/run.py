import requests
import os
from PIL import Image
import base64
from io import BytesIO
import googlemaps
google_api_key = os.environ["GOOGLE_API_KEY"]

API_KEY = os.environ["BASETEN_API_KEY"]
# print(API_KEY)


user_location = (39.9489, -75.1500)

# Get the API key from the environment variable
gmaps = googlemaps.Client(key=google_api_key)
# poi_results = gmaps.places_nearby(
#     location=user_location, radius=100, type="point_of_interest"
# )

# Make a nearby search request for tourist attractions
attraction_results = gmaps.places_nearby(
    location=user_location, radius=100, type="tourist_attraction"
)

region = gmaps.reverse_geocode(user_location)

# Parse the results

for component in region[0]['address_components']:
    if 'country' in component['types']:
        country = component['long_name']
    elif 'administrative_area_level_1' in component['types']:
        state = component['long_name']
    elif 'locality' in component['types']:
        city = component['long_name']

region_string = f'Country: {country}, State: {state}, City: {city}'



attractions = ['The whole place at ']
for place in attraction_results["results"]:
   attractions += [place["name"]]

attraction_strings = []
for s in attractions:
    attraction_strings += [s + ' in ' + region_string + '.']



def get_prompt(string):
# TODO prompt engineering here.
    return f"{string}, as tourist, suitable for display on the mobile device, historical fact."


BASE64_PREAMBLE = "data:image/png;base64,"

def b64_to_pil(b64_str):
    return Image.open(BytesIO(base64.b64decode(b64_str.replace(BASE64_PREAMBLE, ""))))

s = attraction_strings[1]
res = requests.post(
    "https://model-rwnp8z23.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {API_KEY}"},
    json={'prompt': get_prompt(s), 'use_refiner': True},
)

res = res.json()
output = res.get("data")
# print(res)


# import sys
# sys.exit()
# Convert the base64 model output to an image
img = b64_to_pil(output)
img.save("output_image.png")


model_id = "owpj019w"
baseten_api_key = os.environ["BASETEN_API_KEY"]

def base64_to_mp4(base64_string, output_file_path):
    binary_data = base64.b64decode(base64_string)
    with open(output_file_path, "wb") as output_file:
        output_file.write(binary_data)

def mp4_to_base64(file_path: str):
    with open(file_path, "rb") as mp4_file:
        binary_data = mp4_file.read()
        base64_data = base64.b64encode(binary_data)
        base64_string = base64_data.decode("utf-8")

    return base64_string
def image_to_base64(image_path: str):
    with open(image_path, "rb") as image_file:
        binary_data = image_file.read()
        base64_data = base64.b64encode(binary_data)
        base64_string = base64_data.decode("utf-8")

    return base64_string
data = {
  "image": image_to_base64("./output_image.png"),
  "num_frames": 25,
  "decoding_t": 5,
  "duration": 4
}

# Call model endpoint
res = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)

# Get the output of the model
# print(res)
res = res.json()

base64_output = res.get("output")

# Convert the base64 output to an mp4 video
base64_to_mp4(base64_output, "stable-video-diffusion-output.mp4")

# with open('attraction_names.txt', 'w') as f:
#     f.write(s + '\n')