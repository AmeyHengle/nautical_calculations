# nautical_calculations

nautical_calculations is a Python library for dealing with geo-spatial calculations such as bearing, nautical distance, etc.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install nautical_calculations
```

## Usage
```python
import nautical_calculations
```
```python
nautical_calculations.calculate_distance(lat1,long1,lat2,long2) # returns the nautical distance (in km) between two coordinates (lat1,long1) and (lat2,long2)

```
![example](https://github.com/AmeyHengle/nautical_calculations/blob/master/samples/distance.png)


```python

nautical_calculations.calculate_bearing(lat1,long1,lat2,long2) # returns the bearing between two coordinates (lat1,long1) and (lat2,long2)

```
![example1]()

```python

nautical_calculations.get_point(lat,long,azimuth,distance) # returns the coordinate (lat1,long1) at a particular distance and angle (azimuth) from the given point (lat,long)
```
![example1]()

```python

nautical_calculations.divide_by_number(lat1, long1, lat2, long2, number) # returns a list containing all points in between the two specified coordinate pairs (lat-long) given the number value
```
![example1]()


```python

nautical_calculations.divide_by_interval(lat1, long1, lat2, long2, interval) # returns a list containing all points in between the two specified coordinate pairs (lat-long) given the interval value

```
![example1]()

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
