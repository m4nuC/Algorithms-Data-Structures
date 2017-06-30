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
        return 'Idx: {}, Par: {}, L: {}, R: {}, Data:{}'.format(self.index, self.parent, self.left, self.right, self.data)

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

    def max(self, start = 1):
        node = self.nodes[start] if start in self.nodes else None
        last_seen_value = node.data['value']
        while node:
            node = self.nodes[node.right] if node.right else None
            last_seen_value = node.data['value'] if node else last_seen_value
        return last_seen_value

    def min(self, start = 1):
        node = self.nodes[start] if start in self.nodes else None
        last_seen_value = node.data['value']
        while node:
            last_seen_value = node.data['value']
            node = self.nodes[node.left] if node.left else None
        return last_seen_value

    def pred(self, value):
        search_result = self.search(value)
        if search_result[0] == False: return False
        node = search_result[1]
        if node.left:
            return self.max(node.left)
        else:

            parent = self.nodes[node.parent]
            last_seen_value = parent.data['value']
            while parent and parent.data['value'] >= value:
                if parent.parent is None: return False
                parent = self.nodes[parent.parent]
                last_seen_value = parent.data['value'] if parent else last_seen_value
            return last_seen_value


    def search(self, value, current_node = 1):
        node = self.nodes[current_node] if current_node in self.nodes else None
        if not bool(node): return (False, current_node)
        if node.data['value'] == value: return (True, node)
        if node.data['value'] > value:
            return self.search(value, current_node*2)
        elif node.data['value'] <= value:
            return self.search(value, current_node*2+1)

    def search_iter(self, value):
        node = self.nodes[1] if 1 in self.nodes else (False, 1)
        while node:
            if node.data['value'] == value: return node
            elif node.data['value'] > value:
                node = self.nodes[node.left] if node.left else None
            elif node.data['value'] <= value:
                node = self.nodes[node.right]  if node.right else None

    def insert(self, value):
        search_result = self.search(value)
        new_node = None
        if search_result[0]:
            node = search_result[1]
            last_seen_index = node.index
            while node:
                last_seen_index = node.index
                node = self.nodes[node.left] if node.left else None
            new_node = Node(last_seen_index, math.floor(last_seen_index/2), None, None, {'value': value})
            self.nodes[new_node.parent].left = last_seen_index
        else:
            new_node = Node(search_result[1], math.floor(search_result[1]/2), None, None, {'value': value})
            parent = self.nodes[new_node.parent]
            if value > parent.data['value']:
                parent.right = new_node.index
            else:
                parent.left = new_node.index

        print('inserting', new_node, 'at', new_node.index)
        self.nodes[new_node.index] = new_node


    def __str__(self):
        for node in self.nodes:
            print(self.nodes[node])
        return ''

