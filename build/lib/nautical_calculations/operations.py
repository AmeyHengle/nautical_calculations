from math import cos, sin, atan2, radians, degrees, asin, modf
from nautical_calculations.basic import get_bearing, get_distance


# -------------------returns a list containing all points in between the two specified coordinate pairs (lat-long) given the number value-----------

def divide_by_number(lat1, long1, lat2, long2, num):
    try:
        lat1 = float(lat1); long1 = float(long1);  lat2 = float(lat2); long2 = float(long2);
        num = num + 1
        coordinate_list = []
        azimuth = get_bearing(lat1, long1, lat2, long2)
        dist = get_distance(lat1, long1, lat2, long2)
        dist = (dist / num)
        counter = float(dist)
        coordinate_list.append([lat1, long1])
        for distance in range(num - 1):
            coord = get_point(lat1, long1, azimuth, counter)
            counter = counter + float(dist)
            coordinate_list.append(coord)
        coordinate_list.append([lat2, long2])
        return coordinate_list
    except Exception as e:
        return 'Exception: '+ e


# -------------------returns a list containing all points in between the two specified coordinate pairs (lat-long) given the interval value-----------

def divide_by_interval(lat1, long1, lat2, long2, interval):
    try:
        lat1 = float(lat1); long1 = float(long1);  lat2 = float(lat2); long2 = float(long2);
        coordinate_list = []
        azimuth = get_bearing(lat1, long1, lat2, long2)
        d = get_distance(lat1, long1, lat2, long2)
        remainder, dist = modf((d / interval))
        counter = float(interval)
        coordinate_list.append([lat1, long1])
        for distance in range(0, int(dist)):
            coord = get_point(lat1, long1, azimuth, counter)
            counter = counter + float(interval)
            coordinate_list.append(coord)
        coordinate_list.append([lat2, long2])
        return coordinate_list
    except Exception as e:
        return 'Exception: ' + e


# ----------Returns the coordinates of destination point given the start lat, long, azimuth, and distance----------

def get_point(lat, long, azimuth, distance):
    try:
        lat = float(lat); long = float(long);  azimuth = float(azimuth); distance = float(distance)
        R = 6371  # Radius of the Earth in km
        bearing = radians(azimuth)  # Bearing is degrees converted to radians.
        d = distance # Distance in km

        lat1 = radians(lat)  # Current dd lat point converted to radians
        long1 = radians(long)  # Current dd long point converted to radians

        lat2 = asin(sin(lat1) * cos(d / R) + cos(lat1) * sin(d / R) * cos(bearing))

        long2 = long1 + atan2(sin(bearing) * sin(d / R) * cos(lat1),
                              cos(d / R) - sin(lat1) * sin(lat2))

        # convert back to degrees
        lat2 = degrees(lat2)
        long2 = degrees(long2)

        return [lat2, long2]
    except Exception as e:
        return 'Exception: '+e

# ----------Returns the coordinates of midpoint on the great circle joining the given endpoint coordinates (lat1,long1,lat2,long2)----------
def get_midpoint(lat1,long1,lat2,long2):
    try:
        lat1 = float(lat1); long1 = float(long1); lat2 = float(lat2); long2 = float(long2)
        azimuth = get_bearing(lat1,long1,lat2,long2)
        distance = get_distance(lat1,long1,lat2,long2)/2
        coords = get_point(lat1,long1,azimuth,distance)
        return coords
    except Exception as e:
        return 'Exception:' + e

#-----------------Useful conversions-----------------
def convert_to_miles(distance):       #converts distance in kms to miles
    try:
        distance = float(distance)
        return (distance * 0.621371)
    except Exception as e:
        return e

def convert_to_kilometres(distance):        #converts distance on miles to kms
    try:
        distance = float(distance)
        return (distance * 1.60934)
    except Exception as e:
        return e

def convert_to_radians(angle):  #converts angle in degrees to radians
    try:
        angle = float(angle)
        return (angle * 0.0174533)
    except Exception as e:
        return e

def convert_to_degress(angle):  #converts angle in radians to degrees
    try:
        angle = float(angle)
        return (angle * 57.2958)
    except Exception as e:
        return e
#------------------------------------------------------
