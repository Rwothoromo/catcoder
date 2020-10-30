import sys

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')
output = []
network = {}

data = input_file.read().splitlines()
n = int(data[0])
cheapest, cheapest_index = int(data[1]), 0

for i in range(n):
    val = int(data[i+1])
    if val < cheapest:
        cheapest = val
        cheapest_index = i

output_file.write('{}\n'.format(cheapest_index))

output_file.close()
input_file.close()
