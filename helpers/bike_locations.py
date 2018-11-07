import helpers.haversine as haver
import requests


# class BikeStation:
#     def __init__(self, key, name, lat, lng, stands, bikes, status):
#         self.key = key
#         self.name = name
#         self.lat = lat
#         self.lng = lng
#         self.stands = stands
#         self.bikes = bikes
#         self.status = status

def closest_stations(address, bike_data):
    # Covert address from User to Lat and Lng
    coords = get_coordinates(address)
    # Use Haversine Formula to return closest station to address
    closest_stations = haver.closest(bike_data, coords)

    # for station in closest_stations:
    #     station_object = BikeStation(station['number'], station['name'], station['lat'], station['lng'],
    #                                  station['available_bike_stands'], station['available_bikes'], station['status'])
    #     sorted_stations.append(station_object)
    # print(sorted_stations)
    # print(closest_stations)
    return closest_stations


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
