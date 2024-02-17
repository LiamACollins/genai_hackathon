import folium
from selenium import webdriver
from selenium.webdriver.common.by import By
from functools import partial
from tqdm.auto import tqdm

# Get pwd:
import os
import time

pwd = os.getcwd()


def make_image(start_coordinates, end_coordinates, total_frames, indexing_offset, i):
    delta = (
        end_coordinates[0] - start_coordinates[0],
        end_coordinates[1] - start_coordinates[1],
    )
    latitude, longitude = (
        start_coordinates[0] + i * delta[0] / total_frames,
        start_coordinates[1] + i * delta[1] / total_frames,
    )
    containers_map = folium.Map(location=[latitude, longitude], zoom_start=50)
    # Add a blue dot marker for the current location
    folium.Marker(
        location=[latitude, longitude],
        icon=folium.Icon(color="red", icon="person", prefix="fa"),
    ).add_to(containers_map)
    containers_map.save("my_map_%04d.html" % i)

    # Set up the headless browser
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)

    # Open the saved HTML file
    driver.get("file://" + pwd + "/my_map_%04d.html" % i)
    driver.execute_script(
        "arguments[0].setAttribute('style', arguments[1])",
        driver.find_element(By.CSS_SELECTOR, "body"),
        "opacity: 1 !important;",
    )
    # Take a screenshot of the map
    driver.save_screenshot("images/%04d.png" % (i + indexing_offset))

    # Close the browser
    driver.quit()


# Create a pool of workers to execute the make_image function
fps = 20
num_seconds = 12
total_frames1 = fps * num_seconds
make_image1 = partial(
    make_image,
    (39.949205, -75.150204),
    (39.949141, -75.149703),
    total_frames1,
    0,
)
num_seconds = 3
total_frames2 = fps * num_seconds
make_image2 = partial(
    make_image,
    (39.949141, -75.149703),
    (39.949103, -75.149333),
    total_frames2,
    total_frames1,
)
num_seconds = 1
total_frames3 = fps * num_seconds
make_image3 = partial(
    make_image,
    (39.949103, -75.149333),
    (39.949122, -75.149495),
    total_frames3,
    total_frames1 + total_frames2,
)
num_seconds = 2
total_frames4 = fps * num_seconds
make_image4 = partial(
    make_image,
    (39.949122, -75.149495),
    (39.949740, -75.150122),
    total_frames4,
    total_frames1 + total_frames2 + total_frames3,
)
num_seconds = 1
total_frames5 = fps * num_seconds
make_image5 = partial(
    make_image,
    (39.949740, -75.150122),
    (39.949591, -75.150155),
    total_frames5,
    total_frames1 + total_frames2 + total_frames3 + total_frames4,
)
num_seconds = 10
total_frames6 = fps * num_seconds
make_image6 = partial(
    make_image,
    (39.949591, -75.150155),
    (39.949591, -75.150155),
    total_frames6,
    total_frames1 + total_frames2 + total_frames3 + total_frames4 + total_frames5,
)
num_seconds = 9
total_frames7 = fps * num_seconds
make_image7 = partial(
    make_image,
    (39.949591, -75.150155),
    (39.949659, -75.150124),
    total_frames7,
    total_frames1
    + total_frames2
    + total_frames3
    + total_frames4
    + total_frames5
    + total_frames6,
)

for i in tqdm(range(total_frames1)):
    make_image1(i)

for i in tqdm(range(total_frames2)):
    make_image2(i)

for i in tqdm(range(total_frames3)):
    make_image3(i)

for i in tqdm(range(total_frames4)):
    make_image4(i)

for i in tqdm(range(total_frames5)):
    make_image5(i)

for i in tqdm(range(total_frames6)):
    make_image6(i)

for i in tqdm(range(total_frames7)):
    make_image7(i)
