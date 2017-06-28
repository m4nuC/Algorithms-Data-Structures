from functools import reduce
from itertools import chain
import math
from Heap.Heap import MinHeap

debug = False

# lambda acc, next: next if shortest_distance[next[1]] + next[2] < shortest_distance[acc[1]] + acc[2] else acc
def dijkstra(G, start, end):
    """ Original implementation of dijkstra without using a priority queue (Min heap)
        Run time of O(|V|^2)
    """
    vertices = set(G.keys())
    processed = set([start])
    shortest_distance = {}
    shortest_path = {start: []}

    min_heap = MinHeap([(start, 0)])

    for vertex in vertices:
        shortest_distance[vertex] = math.inf
        shortest_path[vertex] = []

    shortest_distance[start] = 0

    def dijkstra_gready_selection(acc, next):
        next_distance = shortest_distance[next[0]] + next[2]
        acc_distance = shortest_distance[acc[0]] + acc[2]
        return next if next_distance < acc_distance else acc


    while (bool(vertices-processed)):

        # Candidate vertices are the one that have at least on edge whos head is not processed (hence it is in graph - processed)
        candidate_vertices = [vertex for vertex in processed if reduce( lambda acc, next: next[0] not in processed or acc, G[vertex])]

        # format all edges as a tuple in the form of: (tail, head, distance)
        candidate_edges = [(vertex, edge[0], edge[1]) for vertex in candidate_vertices for edge in G[vertex]]

        # fitler edges whos tails are in processed
        candidate_edges = [edge for edge in candidate_edges if edge[1] not in processed]

        min_edge_tail, min_edge_head, min_edge_distance = reduce(dijkstra_gready_selection, candidate_edges)

        for tail, head, distance in candidate_edges:
            new_distance = shortest_distance[tail] + distance
            if new_distance < shortest_distance[head]:
                shortest_distance[head] = new_distance
                shortest_path[head] = shortest_path[tail] + [head]

        processed.add(min_edge_head)

    # print('shortest_distance', shortest_distance)
    # print('shortest_path', shortest_path)
    # return (shortest_distance, shortest_path)
    distance = shortest_distance[end] if end in shortest_distance else 1000000
    return distance
