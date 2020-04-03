import sys
import csv

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')

N = int(input_file.readline().rstrip())  # Number of flight entries that follow

flights_dict = {}
duplicate_flights_dict = {}

data = (line.strip() for line in input_file)
lines = (line.split(",") for line in data if line)
with open("input.csv", 'w', newline='') as input_csv:
    writer = csv.writer(input_csv)
    writer.writerows(lines)

with open("input.csv", newline='') as f, open('sorted.csv', 'w', newline='') as final:
    writer = csv.writer(final, delimiter=',')
    reader = csv.reader(f, delimiter=',')
    next(reader)
    sorted_csv = sorted(reader, key=lambda row: (row[4], row[5]))
    writer.writerows(sorted_csv)

input_file = open('sorted.csv', 'r')
for entry in range(N):
    data = input_file.readline().rstrip()
    data_list = [i for i in data.split(',')]

    if data_list != ['']:
        start = data_list[4]
        destination = data_list[5]
        takeoff = data_list[6]

        journey = (start, destination)
        if (journey, takeoff) not in duplicate_flights_dict.keys():
            duplicate_flights_dict[(journey, takeoff)] = journey
            if journey not in flights_dict.keys():
                flights_dict[journey] = 1
            else:
                flights_dict[journey] += 1

for flight in flights_dict.items():
    start, destination = flight[0][0], flight[0][1]
    flight_count = flight[1]
    output_file.write("{} {} {}\n".format(start, destination, flight_count))
