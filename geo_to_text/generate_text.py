import requests
import os
import re
baseten_api_key = os.environ["BASETEN_API_KEY"]

def clean_and_truncate_text(text):
    # Remove HTML tags
    text_without_html = re.sub(r'<.*?>', '', text)
    # Remove [INST]...[/INST] text
    text_without_inst = re.sub(r'\[INST\].*?\[\/INST\]', '', text_without_html)
    # Find the last period in the text
    last_period_index = text_without_inst.rfind('.')
    # Truncate the text up to the last period (if a period is found)
    if last_period_index != -1:
        text_truncated = text_without_inst[:last_period_index + 1]
    else:
        text_truncated = text_without_inst  # Keep the text as is if no period is found
    return text_truncated



def get_prompt(geo_string, user_string):

    return f"Please write a short text that briefly introduces {geo_string} to someone who is a tourist and is taking a walk in the city. {user_string}"

def customized_text_generation(story_option, image_option, geo_string):

    prompt = get_prompt(geo_string, "")
    prompt += f"In addition, ther person loves {story_option} and would like to see it from {geo_string}."
    data = {
        "prompt": prompt,
        "max_new_tokens": 4096,
        "stream": False,
        "temperature": 1.5,
    }
    # llama : 8w67ov0q
    # mistra : 6wglrxv3
    # Call model endpoint
    res = requests.post(
        f"https://model-6wglrxv3.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json=data
    )

    return clean_and_truncate_text(res.json())

if __name__ == "__main__":
    import json 
    # print(customized_text_generation("Historical facts", "Realistic old school photography shot on a kodak camera", "Liberty bell, Philadelphia"))
    # print(customized_text_generation("Historical facts", "Realistic old school photography shot on a kodak camera", "Independence hall, Philadelphia"))

    filename = 'cached_intros.json'

    cache = dict()

    cache['hist_kodak_bell'] = customized_text_generation("Historical facts", "Realistic old school photography shot on a kodak camera", "Liberty bell, Philadelphia")
    cache['hist_kodak_independence'] = customized_text_generation("Historical facts", "Realistic old school photography shot on a kodak camera", "Independence hall, Philadelphia")
    cache['thriller_vibrant_bell'] = customized_text_generation("Mystery Thriller", "Realistic old school photography shot on a kodak camera", "Liberty Bell, Philadelphia")
    cache['thriller_vibrant_independence'] = customized_text_generation('Mystery Thriller', 'Vibrant and animated', 'Independence hall, Philadelphia')


    

    # Save the dictionary to a JSON file
    with open(filename, 'w') as file:
        json.dump(cache, file, indent=4)

    print(f"Dictionary has been saved to {filename}")
