import requests
import os

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/WyUukXkFe5JhCwSLMJJr"

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": os.environ["ELEVENLABS_API_KEY"],
}

data = {
    "text": " The Liberty Bell is a historic symbol of freedom and democracy located in Philadelphia, Pennsylvania. The bell, which was cast in 1776 to celebrate the United States' declaration of independence from Great Britain, has become an iconic landmark and a popular tourist attraction",
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
}

response = requests.post(url, json=data, headers=headers)
with open("output.mp3", "wb") as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
