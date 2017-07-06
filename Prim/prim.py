import sys
from Heap.Heap import MinHeap
from functools import reduce
import math
debug = True

class Searchable_heap(MinHeap):
    def find_value(self, value, start = 0):
        node = self.heap[start] if self.size() > start else None
        if not node: return None
        elif node[0] == value:
            debug and print('found value {} at index {}'.format(node[0], start))
            return start
        else:
            return self.find_value(value, start + 1)


def heapified_prim(graph):
    debug and print('Graph:', graph)
    v = list(graph.keys())
    vertices = set(v)
    explored = set([v[0]])
    unexplored = vertices-explored
    unexplored_heap = Searchable_heap([], lambda x: x[1])
    total_weight = 0

    for vertex in unexplored:
        local_min = math.inf
        for edge in graph[vertex]:
            if edge[0] in explored:
                local_min = min(local_min, edge[1])
        unexplored_heap.add((vertex, local_min))

    while bool(unexplored):
        closest_vertex = unexplored_heap.pluck_min()
        explored.add(closest_vertex[0])
        unexplored.remove(closest_vertex[0])
        total_weight += closest_vertex[1]
        local_min = math.inf
        edges_candidate_for_update  = [edge for edge in graph[closest_vertex[0]] if edge[0] in unexplored]
        for edge in edges_candidate_for_update:
            local_min = math.inf
            for e in graph[edge[0]]:
                if e[0] in explored:
                    local_min = min(local_min, e[1])
            index_to_remove = unexplored_heap.find_value(edge[0])
            unexplored_heap.pluck(index_to_remove)
            unexplored_heap.add((edge[0], local_min))

    return total_weight

def prim(graph):
    v = list(graph.keys())
    vertices = set(v)
    explored = set([v[0]])
    unexplored = vertices-explored
    best_edge = None
    total_weight = 0
    while bool(unexplored):
        for tail in explored:
            for head in graph[tail]:
                if head[0] in unexplored and (not bool(best_edge) or head[1]<best_edge[1]):
                    best_edge = head
        explored.add(best_edge[0])
        unexplored.remove(best_edge[0])
        total_weight += best_edge[1]
        best_edge = None
    return total_weight