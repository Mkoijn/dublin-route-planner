import requests
from math import cos, asin, sqrt


def get_distance(lat1, lon1, lat2, lon2):
    '''
    The haversine formula determines the great-circle
    distance between two points on a sphere given
    their longitudes and latitudes.
    '''
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) \
        * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))


def add_distance(data, v):
    '''
    Adds distance attribute (interspace) from given address
    to a items in a list of stations (data)
    '''
    for station in data:
        interspace = get_distance(v['lat'], v['lng'], station['lat'], station['lng'])
        station.update({'interspace': interspace})
    return data


def closest_stations(address, bike_data):
    # Covert address from User to Lat and Lng
    coords = get_coordinates(address)
    # Use Haversine Formula to return closest station to address
    closest_stations = add_distance(bike_data, coords)
    return closest_stations


def get_coordinates(address):
    # Using googles api translate address to coordinates
    key = 'AIzaSyDbgLgWR25egCX278y1OGq5qFiJs9QQLzc'
    add = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address.replace(' ', '+') + '&key=' + key
    response = requests.get(add)
    resp_json_payload = response.json()
    # Check that there is a result else reload index page
    if resp_json_payload.get('status') != 'ZERO_RESULTS':
        lat = resp_json_payload['results'][0]['geometry']['location']['lat']
        lng = resp_json_payload['results'][0]['geometry']['location']['lng']
    else:
        return
    coords = {'lat': lat, 'lng': lng}
    return coords
