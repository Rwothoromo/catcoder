import sys

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')
data_csv = open('social_network.txt', 'r')
output = []
network = {}

questions = input_file.read().splitlines()
data = data_csv.read().splitlines()
for i in data:
    i_list = i.split(',')
    network[i_list[0]] = i_list[1:]


def str_from_list(x_list):
    if not x_list:
        return None
    return ','.join(x_list)


for j in questions:
    j_list = j.split('(')
    child = j_list[1].split(')')[0]
    if j_list[0] == 'ancestors':
        x = []  # get ancestors from graph
        output_file.write('{}\n'.format(str_from_list(x)))

output_file.close()
input_file.close()
