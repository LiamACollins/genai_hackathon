import requests
import os
import re
baseten_api_key = os.environ["BASETEN_API_KEY"]

def remove_html_and_inst(text):
    # Remove HTML tags
    no_html = re.sub(r'<.*?>', '', text)
    # Remove [INST]...[/INST] including the tags themselves
    no_inst = re.sub(r'\[INST\].*?\[\/INST\]', '', no_html)
    return no_inst
# Replace the empty string with your model id below



def get_prompt(geo_string, user_string):

    return f"Please write a text that briefly introduces {geo_string} to someone who likes {user_string}. The person to be introduced is a tourist and is taking a walk in the area who happens to be nofitied by the app to visit {geo_string}. Do not use excessive expressions."

def customized_text_generation(story_option, image_option, geo_string):
    user_string = story_option
    prompt = get_prompt(geo_string, user_string)
    data = {
        "prompt": prompt,
        "max_new_tokens": 2048,
        "stream": False,
    }
    # llama : 8w67ov0q
    # mistra : 6wglrxv3
    # Call model endpoint
    res = requests.post(
        f"https://model-6wglrxv3.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json=data
    )

    return remove_html_and_inst(res.json())

if __name__ == "__main__":
    import json 
    # print(customized_text_generation("Historical facts", "Realistic old school photography shot on a kodak camera", "Liberty bell, Philadelphia"))
    # print(customized_text_generation("Historical facts", "Realistic old school photography shot on a kodak camera", "Independence hall, Philadelphia"))

    filename = 'cached_intros.json'

    cache = dict()

    cache['hist_kodak_bell'] = customized_text_generation("Historical facts", "Realistic old school photography shot on a kodak camera", "Liberty bell, Philadelphia")
    cache['hist_kodak_independence'] = customized_text_generation("Historical facts", "Realistic old school photography shot on a kodak camera", "Independence hall, Philadelphia")
    cache['thriller_vibrant_bell'] = customized_text_generation('Mystery Thriller', 'Vibrant and animated', 'Liberty bell, Philadelphia')
    cache['thriller_vibrant_independence'] = customized_text_generation('Mystery Thriller', 'Vibrant and animated', 'Independence hall, Philadelphia')


    

    # Save the dictionary to a JSON file
    with open(filename, 'w') as file:
        json.dump(cache, file, indent=4)

    print(f"Dictionary has been saved to {filename}")
