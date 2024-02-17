import googlemaps
import os

# The idea is that we have some sort of user location being pulled by the app
# For now, we'll just use a hardcoded location currently using times square (NYC)
user_location = (40.7554901, -73.9865556)

# Get the API key from the environment variable
api_key = os.environ["GOOGLEPLACES_API_KEY"]
gmaps = googlemaps.Client(key=api_key)
poi_results = gmaps.places_nearby(
    location=user_location, radius=100, type="point_of_interest"
)

# Make a nearby search request for tourist attractions
attraction_results = gmaps.places_nearby(
    location=user_location, radius=100, type="tourist_attraction"
)

print("Point of Interest Results")
for place in poi_results["results"]:
    print(place["name"])

print("\nTourist Attraction Results")
for place in attraction_results["results"]:
    print(place["name"])
