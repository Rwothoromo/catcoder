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


def ancestors(network, child):
    list_of_ancestors = []

    if child in network:
        list_of_ancestors = network[child]
        for ancestor in network[child]:
            for i in ancestors(network, ancestor):
                if i not in list_of_ancestors:
                    list_of_ancestors += ancestors(network, ancestor)
    if list_of_ancestors:
        list_of_ancestors = list(set(list_of_ancestors))
        list_of_ancestors = list(filter(None, list_of_ancestors))
        list_of_ancestors.sort()
    return list_of_ancestors


def descendants(network, child):
    list_of_descendants = []
    if child in network:
        for (key, value) in network.items():
            if child in value:
                list_of_descendants.append(key)
        for descendant in list_of_descendants:
            for i in descendants(network, descendant):
                if i not in list_of_descendants:
                    list_of_descendants += descendants(network, descendant)
    if list_of_descendants:
        list_of_descendants = list(set(list_of_descendants))
        list_of_descendants = list(filter(None, list_of_descendants))
        list_of_descendants.sort()
    return list_of_descendants


def cousins(network, child):
    list_of_cousins = []
    return list_of_cousins


for j in questions:
    j_list = j.split('(')
    child = j_list[1].split(')')[0]
    if j_list[0] == 'ancestors':
        x = ancestors(network, child)
        output_file.write('{}\n'.format(str_from_list(x)))
    if j_list[0] == 'descendants':
        x = descendants(network, child)
        output_file.write('{}\n'.format(str_from_list(x)))
    if j_list[0] == 'cousins':
        x = cousins(network, child)
        output_file.write('{}\n'.format(str_from_list(x)))

output_file.close()
input_file.close()
