import sys
import math

class Node:
    def __init__(self, index, parent, left, right, data):
        self.index = index
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data

    def __str__(self):
        print(self.data)
        return 'Parent: {}, Left: {}, Right: {}, Data:{}'.format(self.parent, self.left, self.right, self.data)

class BST:
    def __init__(self, nodes = {}):
        # Store nodes in a 1 to n indexed dictionary
        if bool(nodes):
            self.nodes = {}
            for key in nodes.keys():
                node = nodes[key]
                self.nodes[key] = Node(key, node[0], node[1], node[2], node[3])
        else:
            self.nodes = nodes

    def left_nodes(self, level = 1):
        if level < 3: return level
        return range(2**level-1, (2**level-2) +1) + self.left_nodes(level+1)

    def right_nodes(self, level = 1):
        if level == 1:
            return 1
        elif level == 2:
            return 3
        return range(2**level-1, (2**level-2) +1) + self.left_nodes(level+1)

    def search(self, value, current_node = 1):
        node = self.nodes[current_node] if current_node in self.nodes else None
        if not bool(node): return (False, current_node)
        if node.data['value'] == value: return (True, current_node)
        if node.data['value'] > value:
            return self.search(value, current_node*2)
        elif node.data['value'] < value:
            return self.search(value, current_node*2+1)

    def search_iter(self, value):
        node = self.nodes[1] if 1 in self.nodes else (False, 1)
        while node:
            if node.data['value'] == value: return node
            elif node.data['value'] > value:
                node = self.nodes[node.left] if node.left else None
            elif node.data['value'] < value:
                node = self.nodes[node.right]  if node.right else None

    def insert(self, value):
        node = self.search(value)
        if node[0]:
            print('there already is such a node')
        else:
            new_node = Node(node[1], math.ceil(node[1]/2)-1, None, None, value)
            self.nodes[node[1]] = new_node

    def __str__(self):
        for node in self.nodes:
            print(self.nodes[node])
        return ''

