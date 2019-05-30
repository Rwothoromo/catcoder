import sys

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')
data_csv = open('social_network.txt', 'r')
output = []


class Graph(object):
    """A simple Graph class"""

    def __init__(self, graph_dict=None):
        """Initialize the graph"""

        self.__graph_dict = {} if graph_dict == None else graph_dict

    def vertices(self):
        """Return the vertices/nodes of the graph"""

        return list(self.__graph_dict.keys())

    def edges(self):
        """Returns the edges (lines between vertices/nodes) of the graph"""

        # separate __generate_edges() because of recursion
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """Add a new vertex/node (with no value) to the graph"""

        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """
        The edge is presumably not a set, tuple or list
        Also, 2 vertices/nodes can have multiple edges in-between them!
        """

        edge = set(edge)
        # get a random vertex/node from the edge and alter edge to exclude popped vertex/node
        vertex = edge.pop()
        next_vertex = edge.pop() if edge else vertex  # if not a loop vs if a loop

        if vertex in self.__graph_dict:
            # append the next vertex/node to the value of vertex in the dictionary
            self.__graph_dict[vertex].append(next_vertex)
        else:
            # assign vertex the value of the next vertex/node
            self.__graph_dict[vertex] = [next_vertex]

    def __generate_edges(self):
        """
        Edges are represented as sets
        with one (a loop back to the vertex) or two vertices
        """

        edges = []
        for vertex in self.__graph_dict:
            for neighbor in self.__graph_dict[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges

    def __str__(self):
        """Generate string representation of the graph"""

        result = "vertices: "
        for item in self.__graph_dict:
            result += "{},".format(item)

        result += "\nedges: "
        for edge in self.__generate_edges():
            result += "{},".format(edge)

        return result

    def find_isolated_vertices(self):
        """Returns list of vertices that are not attached to an edge"""

        graph = self.__graph_dict
        return [vertex for vertex in graph if not graph[vertex]]

    def find_path(self, start_vertex, end_vertex, path=[]):
        """
        Return a path (list of vertices/nodes)
        from where they start to where they end
        """

        graph = self.__graph_dict
        # append only a list containing the start_vertex
        path += [start_vertex]
        if start_vertex == end_vertex:
            return path

        if start_vertex not in graph:
            return None

        # loop through the list of vertices connected to start_vertex
        for vertex in graph[start_vertex]:
            if vertex not in path:
                # start find from this vertex itself
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path

        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """Return a list of all paths from start_vertex to end_vertex"""

        graph = self.__graph_dict
        # append only a list containing the start_vertex
        path += [start_vertex]
        if start_vertex == end_vertex:
            return [path]

        if start_vertex not in graph:
            return []

        # loop through the list of vertices connected to start_vertex
        # and collect the paths therein
        return [path for vertex in graph[start_vertex] if vertex not in path
                for path in self.find_all_paths(vertex, end_vertex, path)]


def generate_graph_dict(data):
    graph_dict = {}
    for i in data:
        i_list = i.split(',')
        child = i_list[0] if i_list[0] != '' else None
        father = i_list[1] if i_list[1] != '' else None
        mother = i_list[2] if i_list[2] != '' else None

        if child:
            parents = []
            if father:
                parents.append(father)
            if mother:
                parents.append(mother)
            graph_dict[child] = parents
    return graph_dict


questions = input_file.read().splitlines()
data = data_csv.read().splitlines()
network = Graph(generate_graph_dict(data))
print(network.__str__())
# print(network.find_all_paths('Abel', None, []))


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
