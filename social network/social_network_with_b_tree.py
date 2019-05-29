import sys

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')
data_csv = open('social_network.txt', 'r')
output = []


class Node:
    """A Basic Node"""

    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data


class BinaryTree:
    """A Binary Tree"""

    def __init__(self):
        self.root = None

    def delete(self):
        self.root = None

    def is_empty(self):
        self.root == None

    def print_tree(self):
        if self.root != None:
            # separate _in_order(self.root) because of recursion
            self._in_order(self.root)

    def _in_order(self, node):
        """In-order Traversal: go Left -> Root -> Right."""
        if node != None:
            self._in_order(node.left)
            print("{} ".format(node.data))
            self._in_order(node.right)

    def _pre_order(self, node):
        """Pre-order Traversal: go Root -> Left -> Right."""

        if node != None:
            print("{} ".format(node.data))
            self._pre_order(node.left)
            self._pre_order(node.right)

    def _post_order(self, node):
        """Post-order Traversal: go Left -> Right -> Root."""

        if node != None:
            self._post_order(node.left)
            self._post_order(node.right)
            print("{} ".format(node.data))

    def find_node(self, data):
        if self.root != None:
            # separate _find_node(data, self.root) because of recursion
            return self._find_node(data, self.root)
        return None

    def _find_node(self, data, node):
        if data == node.data:
            return node
        elif node.left != None:
            return self._find_node(data, node.left)
        elif node.right != None:
            return self._find_node(data, node.right)
        else:
            return None

    def insert_node(self, data, direction):
        if self.root == None:
            self.root = Node(data)
        else:
            # separate _insert_node(data, self.root, direction) because of recursion
            self._insert_node(data, self.root, direction)

    def _insert_node(self, data, node, direction):
        if direction == 'left':
            if node.left != None:
                self._insert_node(data, node.left, 'left')
            else:
                node.left = Node(data)
                node.left.parent = node

        elif direction == 'right':
            if node.right != None:
                self._insert_node(data, node.right, 'right')
            else:
                node.right = Node(data)
                node.right.parent = node

        else:
            if node.data == None:
                self._insert_node(data, node.data, 'node')

    def height(self):
        if self.root != None:
            # separate _height(self, root, 0) because of recursion
            self._height(self.root)
        return 0

    def _height(self, node, height=0):
        if node == None:
            return height

        # increase height to allow proper tabulation/count in the next recursive call
        left_tree_height = self._height(node.left, height + 1)
        right_tree_height = self._height(node.right, height + 1)
        return max(left_tree_height, right_tree_height)

    def find_parent(self, node):
        if node is None:
            return None
        return node.parent


def populate_tree(tree, data):
    for i in data:
        i_list = i.split(',')
        node_data = i_list[0] if i_list[0] != '' else None
        left_data = i_list[1] if i_list[1] != '' else None
        right_data = i_list[2] if i_list[2] != '' else None

        tree.insert_node(node_data, 'node')    # child
        tree.insert_node(left_data, 'left')    # father
        tree.insert_node(right_data, 'right')  # mother
    return tree


questions = input_file.read().splitlines()
data = data_csv.read().splitlines()
initial_data = data[0][0]
network_binary_tree = BinaryTree()
node = network_binary_tree.find_node('Jimmy')

tree = BinaryTree()
network_binary_tree = populate_tree(tree, data)


for j in questions:
    j_list = j.split('(')
    child = j_list[1].split(')')[0]
    if j_list[0] == 'ancestors':
        ancestors = []  # possibly get ancestors from multiple trees
        output_file.write('{}\n'.format(ancestors))

output_file.close()
input_file.close()
