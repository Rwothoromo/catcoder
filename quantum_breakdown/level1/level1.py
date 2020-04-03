import sys

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')

N = int(input_file.readline().rstrip())  # Number of flight entries that follow
timestamps, min_timestamp, max_timestamp = [], None, None
latitudes, min_latitude, max_latitude = [], None, None
longitudes, min_longitude, max_longitude = [], None, None
altitudes, min_altitude, max_altitude = [], 0.0, None

for entry in range(N):
    data = input_file.readline().rstrip()
    data_list = [i for i in data.split(',')]

    # timestamps
    timestamp = int(data_list[0])

    if not min_timestamp:
        min_timestamp = timestamp
    else:
        if timestamp < min_timestamp:
            min_timestamp = timestamp

    if not max_timestamp:
        max_timestamp = timestamp
    else:
        if timestamp > max_timestamp:
            max_timestamp = timestamp

    # latitudes
    latitude = float(data_list[1])

    if not min_latitude:
        min_latitude = latitude
    else:
        if latitude < min_latitude:
            min_latitude = latitude

    if not max_latitude:
        max_latitude = latitude
    else:
        if latitude > max_latitude:
            max_latitude = latitude

    # longitudes
    longitude = float(data_list[2])

    if not min_longitude:
        min_longitude = longitude
    else:
        if longitude < min_longitude:
            min_longitude = longitude

    if not max_longitude:
        max_longitude = longitude
    else:
        if longitude > max_longitude:
            max_longitude = longitude

    # altitudes
    altitude = float(data_list[3])
    if not max_altitude:
        max_altitude = altitude
    else:
        if altitude > max_altitude:
            max_altitude = altitude
    # min_altitude exists as 0 by default

output_file.write("{} {}\n".format(min_timestamp, max_timestamp))
output_file.write("{} {}\n".format(min_latitude, max_latitude))
output_file.write("{} {}\n".format(min_longitude, max_longitude))
output_file.write("{}\n".format(max_altitude))
