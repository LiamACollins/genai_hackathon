import requests
import os
from get_landmarks import get_landmarks


def get_prompt(current_landmark, place):
    prompt = (
        "Produce a captivating digital illustration of the "
        + current_landmark
        + " in "
        + place
        + ". Emphasize its unique architecture and surroundings, and ensure the image is suitable for use as a background in a mobile app."
    )

    return prompt


# The idea is that we have some sort of user location being pulled by the app
# For now, we'll just use a hardcoded location currently using times square (NYC)
user_location = (40.7554901, -73.9865556)
place = "New York City"
# Get the landmarks
landmarks, attractions = get_landmarks(user_location[0], user_location[1])
# Get the prompt for each attraction:
prompts = []
for attraction in attractions:
    prompt = get_prompt(attraction["name"], place)
    prompts.append(prompt)

import requests
import os
import base64
from PIL import Image
from io import BytesIO

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]
BASE64_PREAMBLE = "data:image/png;base64,"


# Function used to convert a base64 string to a PIL image
def b64_to_pil(b64_str):
    return Image.open(BytesIO(base64.b64decode(b64_str.replace(BASE64_PREAMBLE, ""))))


# Prompt for the model
def create_image(i):
    print(prompts[i])
    data = {
        "prompt": prompts[i] + ", detailed, 8K",
        "negative_prompt": "blurry, low quality",
        "steps": 30,
    }

    # Call model endpoint
    res = requests.post(
        f"https://model-2qjd1k2q.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json=data,
    )

    # Get output image
    res = res.json()
    output = res.get("output")

    # Convert the base64 model output to an image
    img = b64_to_pil(output)
    img.save("images/output_image_" + str(i) + ".png")
    # os.system("open output_image.png")


for i in range(len(prompts)):
    create_image(i)
