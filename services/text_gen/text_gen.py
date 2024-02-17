import requests
import os
from services import get_baseten_url, get_baseten_api_key

MISTRAL_MODEL_ID = os.environ["MISTRAL_MODEL_ID"]

def get_mistral_response(prompt: str) -> str:
    url = get_baseten_url(MISTRAL_MODEL_ID)

    resp = requests.post(
        url=url,
        headers={"Authorization": "Api-Key " + get_baseten_api_key()},
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
