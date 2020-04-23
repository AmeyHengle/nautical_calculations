from nautical_calculations.basic import calculate_bearing,calculate_distance
from nautical_calculations.operations import get_point, divide_by_interval, divide_by_number,get_midpoint

def main():
    try:
        while(True):
            print("Enter choice:\n1.Calculate distance\n2.Calculate bearing\n3.Get Point\n4.Divide by number\n5.Divide by interval\n6.Midpoint")
            ch = str(input())
            if(ch == '1'):
                print('Enter coordinates of first point (lat1, long1)')
                lat1 = input(); long1 = input()
                print('Enter coordinates of second point (lat2, long2)')
                lat2 = input(); long2 = input()

                distance = calculate_distance(lat1,long1,lat2,long2)
                print('Nautical distance: ',distance)

            elif (ch == '2'):
                print('Enter coordinates of first point (lat1, long1)')
                lat1 = input(); long1 = input()
                print('Enter coordinates of second point (lat2, long2)')
                lat2 = input(); long2 = input()

                bearing = calculate_bearing(lat1,long1,lat2,long2)
                print('Bearing (degress): ',bearing)

            elif (ch == '3'):
                print('Enter coordinates of start point (lat, long)')
                lat = input(); long = input()
                print('Enter Azimuth (angle) in degrees')
                azimuth = input();
                print('Enter distance in nautical_kms')
                distance = input()

                point = get_point(lat,long,azimuth,distance)
                print('Resultant point: ',point)

            elif (ch == '4'):
                print('Enter coordinates of first point (lat1, long1)')
                lat1 = input(); long1 = input()
                print('Enter coordinates of second point (lat2, long2)')
                lat2 = input(); long2 = input()
                print('Enter number of intermidiate points')
                num = input()

                list = divide_by_number(lat1, long1, lat2, long2,num)
                print('List: \n', list)

            elif (ch == '5'):
                print('Enter coordinates of first point (lat1, long1)')
                lat1 = input();
                long1 = input()
                print('Enter coordinates of second point (lat2, long2)')
                lat2 = input();
                long2 = input()
                print('Enter the value of interval')
                interval = input()

                list = divide_by_interval(lat1, long1, lat2, long2, interval)
                print('List: \n', list)

            elif (ch == '6'):
                print('Enter coordinates of first point (lat1, long1)')
                lat1 = input();
                long1 = input()
                print('Enter coordinates of second point (lat2, long2)')
                lat2 = input();
                long2 = input()
                coords = get_midpoint(lat1, long1, lat2, long2)
                print('Midpoint: \n', coords)

            else:
                print('Invalid command, retry')
                continue

            print('continue? (1/0)')
            ch = str(input())
            if(ch == '0'):
                break


    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()