import sys
from itertools import izip

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')

x_y_data = input_file.readline().rstrip()
x_y_data_list = x_y_data.split(' ')
x, y = int(x_y_data_list[0]), int(x_y_data_list[1])

motion_data = input_file.readline().rstrip()
motion_data_list = motion_data.split(' ')

right_turns = ['right', 'down', 'left', 'up']
down_turns = ['down', 'left', 'up', 'right']
left_turns = ['left', 'up', 'right', 'down']
up_turns = ['up', 'right', 'down', 'left']

position = ''


def pairs(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)


def F(position, n, x, y):
    if position == 'right':
        x += int(j)
    elif position == 'left':
        x -= int(j)
    elif position == 'down':
        y += int(j)
    elif position == 'up':
        y -= int(j)
    return (x, y)


def T(position, turns):
    if position == 'right':
        position = right_turns[turns]
    elif position == 'down':
        position = down_turns[turns]
    elif position == 'left':
        position = left_turns[turns]
    elif position == 'up':
        position = up_turns[turns]
    return position


for i, j in pairs(motion_data_list):
    if not position:
        position = 'right'
    if i == 'T':
        position = T(position, int(j))
    if i == 'F':
        x_y = F(position, int(j), x, y)
        x, y = x_y[0], x_y[1]
        # print(position, int(j), x_y)


# data for output
output_file.write("{} {}\n".format(x, y))

output_file.close()
input_file.close()
