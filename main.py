import os
import sys
from dotenv import load_dotenv
from search import search_nearby_places


def main():
    arguments = sys.argv[1:]
    api_key = os.getenv("GOOGLE_PLACE_API_KEY")
    latitude = os.getenv("LATITUDE")
    longitude = os.getenv("LONGITUDE")
    radius = 2000.0
    included_types = arguments

    results = search_nearby_places(api_key, latitude, longitude, radius, included_types)

    if isinstance(results, dict):
        print("Nearby places:")
        for place in results.get("places", []):
            print(place.get("displayName").get("text"))
    else:
        print("Error:", results)


load_dotenv()

if __name__ == "__main__":
    main()
