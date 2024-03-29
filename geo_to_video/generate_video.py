import base64, requests
from io import BytesIO
from PIL import Image
import os
import uuid
import subprocess

API_KEY = os.environ["BASETEN_API_KEY"]



def get_prompt(geo_string, user_string):
    # TODO prompt engineering here.
    return f"{geo_string}, {user_string}, as tourist, suitable for display on the mobile device, with historical fact."

BASE64_PREAMBLE = "data:image/png;base64,"
def b64_to_pil(b64_str):
    return Image.open(BytesIO(base64.b64decode(b64_str.replace(BASE64_PREAMBLE, ""))))


def base64_to_mp4(base64_string, output_file_path):
    binary_data = base64.b64decode(base64_string)
    with open(output_file_path, "wb") as output_file:
        output_file.write(binary_data)

def mp4_to_base64(file_path: str):
    with open(file_path, "rb") as mp4_file:
        binary_data = mp4_file.read()
        base64_data = base64.b64encode(binary_data)
        base64_string = base64_data.decode("utf-8")

    return base64_string
def image_to_base64(image_path: str):
    with open(image_path, "rb") as image_file:
        binary_data = image_file.read()
        base64_data = base64.b64encode(binary_data)
        base64_string = base64_data.decode("utf-8")

    return base64_string

def generate_video(geo_string, user_string, file_name_prefix = "output"):


    
    res = requests.post(
        "https://model-rwnp8z23.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {API_KEY}"},
        json={'prompt': get_prompt(geo_string, user_string), 'use_refiner': True},
    )

    res = res.json()
    #b64 image
    b64_img_output = res.get("data")

    img = b64_to_pil(b64_img_output)
    img.save(file_name_prefix + "_image.png")

    data = {
    "image": b64_img_output,
    "num_frames": 25,
    "decoding_t": 5,
    "duration": 4
    }

    # Call model endpoint
    res = requests.post(
        f"https://model-owpj019w.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {API_KEY}"},
        json=data
    )

    # Get the output of the model
    # print(res)
    res = res.json()

    base64_output = res.get("output")

    # Convert the base64 output to an mp4 video
    filename = file_name_prefix + "_video.mp4"
    base64_to_mp4(base64_output, filename)
    convert_mp4_to_gif(filename, filename[:-4] + '.gif')



def customized_video_generation(story_option, image_option, geo_string):
    # if story_option == "Historical facts" and image_option == 'Realistic old school photography shot on a kodak camera':
    prompt = geo_string + ', '
    prompt += f'targeted for {story_option} lovers, '
    prompt += f'filmed with {image_option} style, '

    generate_video(geo_string, prompt, file_name_prefix=str(uuid.uuid5(uuid.NAMESPACE_DNS, prompt))[:5])




def convert_mp4_to_gif(input_file, output_file):
    # Command to convert MP4 to GIF using FFmpeg
    # This example uses a simple conversion process.
    # You may want to add additional options to optimize the size and quality of the output GIF.
    cmd = [
        'ffmpeg',
        '-i', input_file,  # Input file
        '-filter_complex', '[0:v] fps=10,scale=480:-1:flags=lanczos,split [a][b];[a] palettegen [p];[b][p] paletteuse',
        '-f', 'gif',  # Output format
        output_file  # Output file
    ]
    
    try:
        # Execute the FFmpeg command
        subprocess.run(cmd, check=True)
        print(f"Conversion successful: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")


if __name__ == "__main__":
    
    # customized_video_generation('Historical facts', 'Realistic old school photography shot on a kodak camera', 'Liberty bell, Philadelphia')
    # customized_video_generation('Historical facts', 'Realistic old school photography shot on a kodak camera', 'Independence hall')

    # customized_video_generation('Mystery Thriller', 'Vibrant and animated', 'Liberty bell, Philadelphia')
    # customized_video_generation('Mystery Thriller', 'Vibrant and animated', 'Independence hall, Philadelphia')

    # historical fact
    # realistic old school photography shot on vintage kodak

    # mistry thriller
    # vibrant and animated

    # poetry run streamlit run home.py

    pass