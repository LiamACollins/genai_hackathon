import requests
import os
import base64
from services import get_baseten_url, get_baseten_api_key

AUDIO_GEN_PROMPT = """
Produce high-quality audio content based on the engaging descriptions of the city's landmarks and attractions.
The audio should be friendly and conversational, suitable for a voice assistant to read out to users during a walking tour.
Ensure that the tone is lively and the pronunciation is accurate, creating an immersive experience for the listeners as they explore the city.
Read the following descriptions:
{}
"""

MELODY_GEN_MODEL_ID = os.environ["MELODY_GEN_MODEL_ID"]

def generate_audio_with_prompt(
        description_prompt: str,
        length_in_seconds: int,
        output_filename: str = "audio.wav"):
    prompt = AUDIO_GEN_PROMPT.format(description_prompt)

    data = {"prompts": [prompt], "duration": length_in_seconds}
    url = get_baseten_url.format(MELODY_GEN_MODEL_ID)
    
    res = requests.post(
        url=url,
        headers={"Authorization": "Api-Key " + get_baseten_api_key()},
        json=data,
    )
    # Print the output of the model
    res = res.json()
    output = res.get("data")

    # Convert the output base64 strings to audio files
    for idx, clip in enumerate(output):
        with open(output_filename, "wb") as f:
            f.write(base64.b64decode(clip))