# nautical_calculations

>nautical_calculations is a Python library used for dealing with some basic Geospatial calculations on the geographic coordinate system. 

>It is developed to act as an interface for performing calculations  like the nautical distance and bearing angle. It explores the possiblitity of using these two basic terms in performing operations like:

>* Finding all the coordinates which lie on the rhumb line joining any two points on the map
>* Finding the coordinates of a point at a particular angle and distance from the given point.
>* Finding the coordinates of midpoint on the rhumb line joining any two points on the map.

>The main idea is to save the time of defining your own functions to derive these terms, thus making the project development easier.

<img alt = 'example1' src = "https://github.com/AmeyHengle/nautical_calculations/blob/master/samples/distance.png" width="300" height = "250"/>
<img alt = 'example2' src = "https://github.com/AmeyHengle/nautical_calculations/blob/master/samples/number.png" width="300" height = "250"/>
<img alt = 'example3' src = "https://github.com/AmeyHengle/nautical_calculations/blob/master/samples/midpoint.png" width="300" height = "250"/> 


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
from nautical_calculations.basic import calculate_distance

from nautical_calculations.basic import calculate_bearing

from nautical_calculations.operations import get_point

from nautical_calculations.operations import get_midpoint

from nautical_calculations.operations import divide_by_interval

from nautical_calculations.operations import divide_by_number
```
## Usage examples:

I) Nautical distance (km)
```python
calculate_distance(lat1,long1,lat2,long2) # returns the nautical distance (in km) between two coordinates (lat1,long1) and (lat2,long2)
```


II) Bearing (degrees)
```python
calculate_bearing(lat1,long1,lat2,long2) # returns the bearing between two coordinates (lat1,long1) and (lat2,long2)
```


III) Point (lat,long)
```python
get_point(lat,long,azimuth,distance) # returns the coordinate (lat1,long1) at a particular distance and angle (azimuth) from the given point (lat,long)
```


IV) Intermediate points (by number)
```python
divide_by_number(lat1, long1, lat2, long2, number) # returns a list containing all points in between the two specified coordinate pairs (lat-long) given the number value
```

V) Intermediate points (by interval)
```python
divide_by_interval(lat1, long1, lat2, long2, interval) # returns a list containing all points in between the two specified coordinate pairs (lat-long) given the interval value
```

VI) Midpoint
```python
get_midpoint(lat1, long1, lat2, long2) #Returns the coordinates of midpoint on the rhumb line joining the given endpoint coordinates (lat1,long1,lat2,long2)
```

VII) Conversions
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

## License
[MIT](https://choosealicense.com/licenses/mit/)

