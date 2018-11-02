def middle_lat_lon(lat1, lon1, lat2, lon2):
    '''
    The haversine formula determines the great-circle
    distance between two points on a sphere given
    their longitudes and latitudes.
    '''
    middle_lat = (lat1 + lat2) / 2
    middle_lon = (lon1 + lon2) / 2
    return [middle_lat, middle_lon]
