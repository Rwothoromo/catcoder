import sys
# from itertools import izip
import math

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')

row_col_data = input_file.readline().rstrip()
row_col_data_list = row_col_data.split(' ')
rows, cols = int(row_col_data_list[0]), int(row_col_data_list[1])

h_min, h_max, h_sum = 0, 0, 0
height_data = []

for i in range(rows):
    heights = input_file.readline().rstrip()
    heights_data_list = heights.split(' ')
    heights_list = [int(x) for x in heights_data_list]

    i_h_min = min(heights_list)
    i_h_max = max(heights_list)
    h_sum += sum(heights_list)

    if i_h_min < h_min:
        h_min = i_h_min
    if i_h_max > h_max:
        h_max = i_h_max

    height_data += heights_list

h_avg = int(math.floor(h_sum / (cols * rows)))

output_file.write("{} {} {}\n".format(h_min, h_max, h_avg))

# def pairs(iterable):
#     "s -> (s0, s1), (s2, s3), (s4, s5), ..."
#     a = iter(iterable)
#     return izip(a, a)
