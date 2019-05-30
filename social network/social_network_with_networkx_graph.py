import networkx as nx
import sys

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')
data_csv = open('social_network.txt', 'r')
output = []


def str_from_list(x_list, exclude=None):
    if not x_list:
        return None

    if exclude:
        x_list.remove(exclude)
    return ','.join(x_list)


def populate_nx_graph(graph, data):
    nodes = []
    edges = []

    for i in data:
        i_list = i.split(',')
        child = i_list[0] if i_list[0] != '' else None
        father = i_list[1] if i_list[1] != '' else None
        mother = i_list[2] if i_list[2] != '' else None

        if child:
            nodes.append(child)
            if father:
                edges.append((child, father))
            if mother:
                edges.append((child, mother))

    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    return graph


questions = input_file.read().splitlines()
data = data_csv.read().splitlines()

graph = nx.DiGraph()
graph = populate_nx_graph(graph, data)


for j in questions:
    j_list = j.split('(')
    child = j_list[1].split(')')[0]
    if j_list[0] == 'ancestors':
        ancestors = nx.shortest_path(graph, child, target=None)
        x_list = [i for i in ancestors]  # get ancestors from graph
        x_list.sort()
        output_file.write('{}\n'.format(str_from_list(x_list, 'Abel')))

output_file.close()
input_file.close()