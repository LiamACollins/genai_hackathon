import requests
import os
from PIL import Image
import base64
from io import BytesIO
from services import get_baseten_url, get_baseten_api_key

SD_TTI_MODEL_ID = os.environ["SD_TTI_MODEL_ID"]
SD_ITV_MODEL_ID = os.environ["SD_ITV_MODEL_ID"]

BASE64_PREAMBLE = "data:image/png;base64,"

def b64_to_pil(b64_str: str):
    return Image.open(BytesIO(base64.b64decode(b64_str.replace(BASE64_PREAMBLE, ""))))

def base64_to_mp4(base64_string, output_file_path):
    binary_data = base64.b64decode(base64_string)
    with open(output_file_path, "wb") as output_file:
        output_file.write(binary_data)

def text_to_image(prompt: str, filename: str = "output_image.png"):
    url = get_baseten_url(SD_TTI_MODEL_ID)

    res = requests.post(
        url,
        headers={"Authorization": f"Api-Key {get_baseten_api_key()}"},
        json={'prompt': prompt, 'use_refiner': True},
    )

    res = res.json()
    #b64 image
    b64_img_output = res.get("data")

    img = b64_to_pil(b64_img_output)
    img.save(filename)

def image_to_video(image_filename: str,
                   num_frames: int = 25,
                   decoding_t: int = 5,
                   duration_s: int = 4,
                   video_filename: str = "stable-video-diffusion-output.mp4"):
    with open(image_filename, "rb") as imgfile:
        img = imgfile.read()
        b64_img = base64.b64encode(img).decode('utf-8')

    data = {
        "image": b64_img,
        "num_frames": num_frames,
        "decoding_t": decoding_t,
        "duration": duration_s
    }

    # Call model endpoint
    url = get_baseten_url(SD_ITV_MODEL_ID)
    res = requests.post(
        url,
        headers={"Authorization": f"Api-Key {get_baseten_api_key()}"},
        json=data
    )

    # Get the output of the model
    # print(res)
    res = res.json()

    base64_output = res.get("output")

    # Convert the base64 output to an mp4 video
    base64_to_mp4(base64_output, video_filename)