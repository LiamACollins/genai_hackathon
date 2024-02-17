import os
import googlemaps

def __get_gmaps_client_instance():
    api_key = os.environ["GOOGLEPLACES_API_KEY"]
    gmaps = googlemaps.Client(key=api_key)
    return gmaps
