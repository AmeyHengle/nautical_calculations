# nautical_calculations

>nautical-calculations is a Python library used for dealing with some basic Geospatial calculations on the geographic coordinate system. 

>It is developed to act as an interface for performing calculations like the nautical distance (Great Circle distance), Rhumb line distance and bearing angle. It explores the possiblitity of using these basic terms in performing operations like:

>* Finding all the coordinates which lie on the great circle line joining any two points on the map
>* Finding the coordinates of a point at a particular angle and distance from the given point.
>* Finding the coordinates of midpoint on the great circle line joining any two points on the map.

>The main idea is to save the time of defining your own functions to derive these terms, thus making the project development easier.

<<<<<<< HEAD
<img src = "https://github.com/AmeyHengle/nautical_calculations/blob/master/samples/distance.png" width="300" height = "250"/> <img src = "https://github.com/AmeyHengle/nautical_calculations/blob/master/samples/number.png" width="300" height = "250"/> <img src = "https://github.com/AmeyHengle/nautical_calculations/blob/master/samples/midpoint.png" width="300" height = "250"/> 
=======
<img alt = 'example1' src = "https://github.com/AmeyHengle/nautical_calculations/blob/master/samples/distance.png" width="300" height = "250"/>       <img alt = 'example2' src = "https://github.com/AmeyHengle/nautical_calculations/blob/master/samples/number.png" width="300" height = "250"/>       <img alt = 'example3' src = "https://github.com/AmeyHengle/nautical_calculations/blob/master/samples/midpoint.png" width="300" height = "250"/> 
>>>>>>> e7618dc58e93ecec3f59e36d7e14040df963347b


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nautical_calculations.

```bash
pip install nautical_calculations
```

## Usage
```python
from nautical_calculations import *
```
or
```python
from nautical_calculations.basic import get_distance

from nautical_calculations.basic import get_bearing

from nautical_calculations.basic import rhumb_line

from nautical_calculations.operations import get_point

from nautical_calculations.operations import get_midpoint

from nautical_calculations.operations import divide_by_interval

from nautical_calculations.operations import divide_by_number
```
## Usage examples:

I) Nautical distance (km)
```python
get_distance(lat1,long1,lat2,long2) # returns the nautical distance (in km) between two coordinates (lat1,long1) and (lat2,long2)
```


II) Bearing (degrees)
```python
get_bearing(lat1,long1,lat2,long2) # returns the bearing between two coordinates (lat1,long1) and (lat2,long2)
```

III) Rhumb Line (km)
```python
rhumb_line(lat1, long1, lat2, long2)   # returns rhumb line distance (in km) between two given coordinates
```

IV) Point (lat,long)
```python
get_point(lat,long,azimuth,distance) # returns the coordinate (lat1,long1) at a particular distance and angle (azimuth) from the given point (lat,long)
```


V) Intermediate points (by number)
```python
divide_by_number(lat1, long1, lat2, long2, number) # returns a list containing all points in between the two specified coordinate pairs (lat-long) given the number value
```

VI) Intermediate points (by interval)
```python
divide_by_interval(lat1, long1, lat2, long2, interval) # returns a list containing all points in between the two specified coordinate pairs (lat-long) given the interval value
```

VII) Midpoint
```python
get_midpoint(lat1, long1, lat2, long2) #Returns the coordinates of midpoint on the rhumb line joining the given endpoint coordinates (lat1,long1,lat2,long2)
```

VIII) Conversions
```python
from nautical_calculations.operations import convert_to_radians,convert_to_miles,convert_to_kilometres,convert_to_degress
```
```python
convert_to_miles(distance)             #converts distance in kms to miles
```
```python
convert_to_kilometres(distance)        #converts distance in miles to kms
```
```python
convert_to_radians(angle)              #converts angle in degrees to radians
```
```python
convert_to_degress(angle)              #converts angle in radians to degrees
```

## Sample code link
https://github.com/AmeyHengle/nautical_calculations/blob/master/nautical_calculations/sample_code.py


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## References
<<<<<<< HEAD
=======

>>>>>>> e7618dc58e93ecec3f59e36d7e14040df963347b
1) http://mathforum.org/library/drmath/view/51879.html
2) http://www.edwilliams.org/avform.htm#Intermediate
3) http://mathforum.org/library/drmath/view/55417.html
4) http://mathforum.org/library/drmath/view/51822.html

## License
[MIT](https://choosealicense.com/licenses/mit/)



