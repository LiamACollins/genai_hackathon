import requests
import os
import base64
from get_cool_landmark_descriptions import get_cool_landmark_descriptions

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

output_from_llm = get_cool_landmark_descriptions()
print("Output from LLM: ", output_from_llm)

print("Generating audio clips...")
prompt = (
    "Produce high-quality audio content based on the engaging descriptions of the city's landmarks and attractions. The audio should be friendly and conversational, suitable for a voice assistant to read out to users during a walking tour. Ensure that the tone is lively and the pronunciation is accurate, creating an immersive experience for the listeners as they explore the city. Read the following descriptions:"
    + output_from_llm
)

# Count number of words in output_from_llm
word_count = len(output_from_llm.split())
# Assume 4 words per second
num_seconds = word_count / 4

# data = {"prompts": ["dog barking"], "duration": 8}
data = {"prompts": [prompt], "duration": num_seconds}

# Call model endpoint
res = requests.post(
    "https://model-4q95xe6w.api.baseten.co/production/predict",
    headers={"Authorization": "Api-Key " + os.environ["BASETEN_API_KEY"]},
    json=data,
)
# Print the output of the model
res = res.json()
output = res.get("data")

# Convert the output base64 strings to audio files
for idx, clip in enumerate(output):
    with open(f"clip_{idx}.wav", "wb") as f:
        f.write(base64.b64decode(clip))
