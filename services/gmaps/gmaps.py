from services.gmaps import __get_gmaps_client_instance
from services.text_gen import text_gen

GET_GUIDE_PROMPT = """
Create engaging and friendly descriptions of the city's landmarks and attractions that are perfect for a walking tour app.
The content should be interesting and informative, providing unique tidbits and stories about each location.
Ensure that the language is conversational and well-suited for being read out loud by a voice assistant, making the experience enjoyable for the users.
We are currently in {0}.
Here are some of the landmarks and attractions around us:
{1}
"""

"""
Usage: 
from services.gmaps import gmaps
results = gmaps.get_nearby_landmarks(
    lat=40.7554901, lng=-73.9865556,
    location_types=['point_of_interest'],
    radius=100)
"""
def get_nearby_landmarks(lat, lng: float, location_types: list[str], radius=50):
    gmaps = __get_gmaps_client_instance()
    response = gmaps.places_nearby(
        location=(lat, lng), radius=radius, type=location_types
    )

    results = {}
    for loc in response['results']:
        results[loc['place_id']] = {
            'place_id': loc['place_id'],
            'name': loc['name'],
            'lat': loc['geometry']['location']['lat'],
            'lng': loc['geometry']['location']['lng']
        }

    return results

"""
Usage:
from services.gmaps import gmaps
desc = gmaps.get_aggregate_text_description(
    40.7554901, -73.9865556, "New York City",
    ['point_of_interest', 'tourist_attraction'])

print(desc)
"""
def get_aggregate_text_description(
        lat, lng: float, current_place_name: str, location_types: list[str], radius=50) -> str:
    landmarks = get_nearby_landmarks(lat, lng, location_types, radius)
    landmark_names = ", ".join([loc['name'] for loc in landmarks.values()])
    prompt = GET_GUIDE_PROMPT.format(current_place_name, landmark_names)

    return text_gen.get_mistral_response(prompt)