import os

__BASETEN_URL = "https://model-{}.api.baseten.co/production/predict"

def get_baseten_url(model_id: str):
    return __BASETEN_URL.format(model_id)

def get_baseten_api_key():
    return os.environ["BASETEN_API_KEY"]