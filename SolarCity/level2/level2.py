import sys
import math
from collections import OrderedDict

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')

row_col_data = input_file.readline().rstrip()
row_col_data_list = row_col_data.split(' ')
rows, cols = int(row_col_data_list[0]), int(row_col_data_list[1])

country_dict = OrderedDict()
height_country_pairs = []


class Cell:
    def __init__(self, x, y, height, country):
        self.x = x
        self.y = y
        self.height = height
        self.country = country

    def is_border(self, grid):
        return self.x - 1 < 0 or self.x + 1 >= rows or self.y - 1 < 0 or self.y + 1 >= cols \
                or grid[self.x - 1][self.y].country != self.country or grid[self.x + 1][self.y].country != self.country \
                or grid[self.x][self.y - 1].country != self.country or grid[self.x][self.y + 1].country != self.country

    def __repr__(self):
        return str([self.x, self.y, self.height, self.country])


def pairs(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)


cell_grid = []
for i in range(rows):
    values = input_file.readline().rstrip()
    values_data_list = values.split(' ')
    height_country_list = [int(x) for x in values_data_list]
    height_country_pairs = pairs(height_country_list)

    cell_grid.append([])

    for j in range(cols):
        cell_grid[i].append(
            Cell(i, j, height_country_pairs[j][0], height_country_pairs[j][1]))

borders_dict = {}
for row in cell_grid:
    for cell in row:
        if cell.is_border(cell_grid):
            if cell.country in borders_dict:
                borders_dict[cell.country] += 1
            else:
                borders_dict[cell.country] = 1

# print([i for i in cell_grid])
for _, borders in borders_dict.items():
    output_file.write("{}\n".format(borders))
