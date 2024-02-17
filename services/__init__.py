__BASETEN_URL = "https://model-{}.api.baseten.co/production/predict"

def get_baseten_url(model_id: str):
    return __BASETEN_URL.format(model_id)