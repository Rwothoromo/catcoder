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


def ancestors(network, child):
    list_of_ancestors = []

    if child in network:
        list_of_ancestors = network[child]
        for x in network[child]:
            for i in ancestors(network, x):
                if i not in list_of_ancestors:
                    list_of_ancestors += ancestors(network, x)
    if list_of_ancestors:
        list_of_ancestors = list(set(list_of_ancestors))
        list_of_ancestors = list(filter(None, list_of_ancestors))
        list_of_ancestors.sort()
    return list_of_ancestors

def str_ancestors(x_ancestors):
    if not x_ancestors:
        return None
    return ','.join(x_ancestors)


for j in questions:
    j_list = j.split('(')
    if j_list[0] == 'ancestors':
        child = j_list[1].split(')')[0]
        x = ancestors(network, child)
        output_file.write('{}\n'.format(str_ancestors(x)))

output_file.close()
input_file.close()
