import json
import urllib.request as url_req
import time
import pandas as pd
from config.api import APIKey

NATAL_CENTER = (-5.8157728,-35.2851133)
API_KEY = APIKey
API_NEARBY_SEARCH_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
RADIUS = 30000
PLACES_TYPES = [('airport', 1), ('bank', 2)] ## TESTING

# PLACES_TYPES = [('airport', 1), ('bank', 2), ('bar', 3), ('beauty_salon', 3), ('book_store', 1), ('cafe', 1), ('church', 3), ('doctor', 3), ('dentist', 2), ('gym', 3), ('hair_care', 3), ('hospital', 2), ('pharmacy', 3), ('pet_store', 1), ('night_club', 2), ('movie_theater', 1), ('school', 3), ('shopping_mall', 1), ('supermarket', 3), ('store', 3)]

def request_api(url):
    response = url_req.urlopen(url)
    json_raw = response.read()
    json_data = json.loads(json_raw)
    return json_data

def get_places(types, pages):
    location = str(NATAL_CENTER[0]) + "," + str(NATAL_CENTER[1])
    mounted_url = ('%s'
        '?location=%s'
        '&radius=%s'
        '&type=%s'
        '&key=%s') % (API_NEARBY_SEARCH_URL, location, RADIUS, types, API_KEY)
    
    results = []
    next_page_token = None

    if pages == None: pages = 1

    for num_page in range(pages):
        if num_page == 0:
            api_response = request_api(mounted_url)
            results = results + api_response['results']
        else:
            page_url = ('%s'
                '?key=%s'
                '&pagetoken=%s') % (API_NEARBY_SEARCH_URL, API_KEY, next_page_token)
            api_response = request_api(str(page_url))
            results += api_response['results']

        if 'next_page_token' in api_response:
            next_page_token = api_response['next_page_token']
        else: break
        
        time.sleep(1)
    return results

def parse_place_to_list(place, type_name):
    # Using name, place_id, lat, lng, rating, type_name
    return [
        place['name'],
        place['place_id'],
        place['geometry']['location']['lat'],
        place['geometry']['location']['lng'],
        type_name       
    ]

def mount_dataset():
    data = []

    for place_type in PLACES_TYPES:
        type_name = place_type[0]
        type_pages = place_type[1]

        print("Getting into " + type_name)

        result = get_places(type_name, type_pages)
        result_parsed = list(map(lambda x: parse_place_to_list(x, type_name), result))
        data += result_parsed

    dataframe = pd.DataFrame(data, columns=['place_name', 'place_id', 'lat', 'lng', 'type'])
    dataframe.to_csv('data/places.csv')

mount_dataset()
