from services.gmaps import __get_gmaps_client_instance

"""
from services.gmaps import gmaps
results = gmaps.get_nearby_locations(
    lat=40.7554901, lng=-73.9865556,
    location_types=['point_of_interest'],
    radius=100)
"""

def get_nearby_locations(lat, lng: float, location_types: list[str], radius=100) -> dict[str, dict]:
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