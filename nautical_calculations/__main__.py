import sys
from logging import log
from nautical_calculations.basic import calculate_bearing,calculate_distance
from nautical_calculations.operations import get_point, divide_by_interval, divide_by_number,get_midpoint


def main():
    try:
        if len(sys.argv) > 1:
            arg = sys.argv[1]
            if arg == 1:
                log('Nautical Distance')
                result = calculate_distance(float(sys.argv[2]), float(sys.argv[3]),float( sys.argv[4]),float( sys.argv[5]))
                print('Nautical Distance (km): ', result)
            elif arg == 2:
                log('bearing')
                result = calculate_bearing(float(sys.argv[2]), float(sys.argv[3]),float( sys.argv[4]),float( sys.argv[5]))
                print('Bearing: ', result)
            elif arg == 3:
                log('get_point')
                result = get_point(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
                print('Resultant point: ', result)
            elif arg == 4:
                log('divide_by_number')
                result = divide_by_number(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
                print('Resultant points:', result)
            elif arg == 5:
                log('divide_by_interval')
                result = divide_by_interval(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
                print('Resultant points: ', result)
            elif arg == 6:
                log('Midpoint')
                result = get_midpoint(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
                print('Resultant point: ', result)

        else:
            print('Welcome to nautical_calculations')

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()