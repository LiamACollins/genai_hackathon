import requests
import os
from get_landmarks import get_landmarks


# TODO: create proper arguments for this function
def get_cool_landmark_descriptions():
    # The idea is that we have some sort of user location being pulled by the app
    # For now, we'll just use a hardcoded location currently using times square (NYC)
    user_location = (40.7554901, -73.9865556)
    place = "New York City"
    # Get the landmarks
    landmarks, attractions = get_landmarks(user_location[0], user_location[1])
    prompt = (
        "Create engaging and friendly descriptions of the city's landmarks and attractions that are perfect for a walking tour app. The content should be interesting and informative, providing unique tidbits and stories about each location. Ensure that the language is conversational and well-suited for being read out loud by a voice assistant, making the experience enjoyable for the users. We are currently in "
        + place
        + ". Here are some of the landmarks and attractions around us: "
    )
    for attraction in attractions:
        prompt += attraction["name"] + ", "

    # Remove the last comma and space
    prompt = prompt[:-2]
    prompt += "."

    resp = requests.post(
        "https://model-7wl17kvq.api.baseten.co/production/predict",
        headers={"Authorization": "Api-Key " + os.environ["BASETEN_API_KEY"]},
        json={
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        },
    )

    return resp.json()
