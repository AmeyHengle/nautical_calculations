import sys
from logging import log
from nautical_calculations.basic import get_distance, get_bearing
from nautical_calculations.operations import calculate_point, divide_by_interval, divide_by_number


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == 1:
            log('Nautical Distance')
            result = get_distance(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
            print('Nautical Distance (km): ', result)
        elif arg == 2:
            log('bearing')
            result = get_bearing(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
            print('Bearing: ', result)
        elif arg == 3:
            log('calculate_point')
            result = calculate_point(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
            print('Resultant point: ', result)
        elif arg == 4:
            log('divide_by_number')
            result = divide_by_number(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
            print('Resultant points:', result)
        elif arg == 5:
            log('divide_by_interval')
            result = divide_by_interval(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
            print('Resultant points: ', result)

    else:
        print('Welcome to nautical_calculations')

if __name__ == '__main__':
    main()