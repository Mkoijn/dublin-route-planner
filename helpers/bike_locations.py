from urllib.request import Request, urlopen
from json import loads
import helpers.haversine as hav
import requests


class BikeStation:
    def __init__(self, key, name, lat, lng, stands, bikes, status):
        self.key = key
        self.name = name
        self.lat = lat
        self.lng = lng
        self.stands = stands
        self.bikes = bikes
        self.status = status


# Bike data URL API
url = 'https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=7453c07d7cf230540911a81515a937d8963cbdfe'

req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows\
                        NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
bike_data = loads(urlopen(req).read().decode("utf-8"))

# get coords of stations from bike data to calculate distances
for item in bike_data:
    item['lat'] = item['position']['lat']
    item['lng'] = item['position']['lng']
    item.pop('position', None)


def closest_station(address):
    coords = get_coordinates(address)
    # Use Haversine Formula to return closest station to address
    closest_station = hav.closest(bike_data, coords)
    station = BikeStation(closest_station['number'], closest_station['name'], closest_station['lat'], closest_station['lng'],
                          closest_station['available_bike_stands'], closest_station['available_bikes'], closest_station['status'])
    return station


def get_coordinates(address):
    # Using googles api translate address to coordinates
    key = 'AIzaSyDbgLgWR25egCX278y1OGq5qFiJs9QQLzc'
    # print(address)
    add = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address.replace(' ', '+') + '&key=' + key
    response = requests.get(add)
    # print(add)
    resp_json_payload = response.json()
    # print(resp_json_payload)
    # print(resp_json_payload['results'][0]['geometry']['location']['lat'])
    lat = resp_json_payload['results'][0]['geometry']['location']['lat']
    lng = resp_json_payload['results'][0]['geometry']['location']['lng']
    coords = {'lat': lat, 'lng': lng}
    return coords
