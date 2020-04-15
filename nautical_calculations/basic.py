from math import cos, sin, atan2, sqrt, radians, degrees, log, tan, pi

#------------Function to calculate the nautical distance (in km) between two given coordinates----------------
def get_distance(lat1, long1, lat2, long2):
    try:
        R = 6371000  # Radius of earth in metres
        lat1rads = radians(lat1)
        lat2rads = radians(lat2)
        deltalat = radians((lat2 - lat1))
        deltalong = radians((long2 - long1))
        a = sin(deltalat / 2) * sin(deltalat / 2) + cos(lat1rads) * cos(lat2rads) * sin(deltalong / 2) * sin(deltalong / 2)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        d = R * c
        return d
    except Exception as e:
        return 'Exception: '+e

#------------Function to calculate the bearing between two given coordinates----------------
def get_bearing(lat1, long1, lat2, long2):
    try:
        startlat = radians(lat1)
        startlong = radians(long1)
        endlat = radians(lat2)
        endlong = radians(long2)
        dlong = endlong - startlong
        dPhi = log(tan(endlat / 2.0 + pi / 4.0) / tan(startlat / 2.0 + pi / 4.0))
        if abs(dlong) > pi:
            if dlong > 0.0:
                dlong = -(2.0 * pi - dlong)
            else:
                dlong = (2.0 * pi + dlong)
        bearing = (degrees(atan2(dlong, dPhi)) + 360.0) % 360.0;
        return bearing
    except Exception as e:
        return 'Exception: '+e