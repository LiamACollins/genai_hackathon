import googlemaps
import os


def get_landmarks(latitude, longitude):
    user_location = (latitude, longitude)
    # Get the API key from the environment variable
    api_key = os.environ["GOOGLEPLACES_API_KEY"]
    gmaps = googlemaps.Client(key=api_key)
    poi_results = gmaps.places_nearby(
        location=user_location, radius=1000, type="point_of_interest"
    )

    # Make a nearby search request for tourist attractions
    attraction_results = gmaps.places_nearby(
        location=user_location, radius=1000, type="tourist_attraction"
    )

    return poi_results["results"], attraction_results["results"]
