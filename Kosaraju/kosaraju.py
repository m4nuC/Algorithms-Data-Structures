import sys
import resource
from collections import OrderedDict

node_by_time = {}
end_time = 0

# Sweet and tiny classic recursive DFS
def dfs(G, start, explored):
    explored.add(start)
    SCC = []
    for vertex in G[start][1]:
        if vertex not in explored:
            SCC.append(vertex)
            dfs(G, vertex, explored)
    return SCC

# modifed DFS to follow incoming edge (emulates running DFS on a reverse Graph)
# Sets end timestamp to use as entry point on DFS second pass
def dfs_reverse(graph, start, explored = set()):
    global end_time
    # if start in explored: return explored
    explored.add(start)
    for node in graph[start][0]:
        if node not in explored:
            dfs_reverse(graph, node, explored)
    end_time += 1
    node_by_time[end_time] = start
    return explored


# same but iterrative (cause python can't handle large recusion trees)
def iter_dfs(G, start, explored):
    global end_time
    explored.add(start)
    stack = [start]
    sccs = set()
    while(len(stack) > 0):
        current = stack[-1]
        explored.add(current)
        next_vertices = [v for v in G[current][1] if v not in explored]
        if len(next_vertices) == 0:
            sccs.add(stack[-1])
            del stack[-1]
        else:
            stack.extend(next_vertices)
    return sccs

# same but iterrative (cause python can't handle large recusion trees)
def iter_dfs_reverse(G, start, explored):
    global end_time
    explored.add(start)
    stack = [start]
    while(len(stack) > 0):
        current = stack[-1]
        explored.add(current)
        next_vertices = [v for v in G[current][0] if v not in explored]
        if len(next_vertices) == 0:
            stack.pop()
            # print('finished with childs of', current)
            end_time += 1
            node_by_time[end_time] = current
        else:
            for v in next_vertices:
                # This check make the running much much slower (Proof?) but is essential for some edge cases
                if v in stack:
                    stack.remove(v)
                stack.append(v)

# For large N Python can't handle recursion depth so iteration is the only way out
def iter_kosaraju(graph):
    explored = set()
    SCCs = []
    vertices = list(graph.keys())
    for i in range(len(vertices)-1,0,-1):
        vertex = vertices[i]
        if vertex not in explored:
            # can be switched from iterration to recurrence
            iter_dfs_reverse(graph, vertex, explored)
    end_times = list(node_by_time.keys())
    explored = set()
    for i in range(len(end_times),0,-1):
        vertex = node_by_time[i]
        if vertex not in explored:
            # can be switched from iterration to recurrence
            SCCs.append(iter_dfs(graph, vertex, explored))

    return SCCs

def kosaraju(graph):
    explored = set()
    SCCs = []
    vertices = list(graph.keys())
    for i in range(len(vertices)-1,0,-1):
        vertex = vertices[i]
        if vertex not in explored:
            # can be switched from iterration to recurrence
            dfs_reverse(graph, vertex, explored)
    end_times = list(node_by_time.keys())
    explored = set()
    for i in range(len(end_times),0,-1):
        vertex = node_by_time[i]
        if vertex not in explored:
            # can be switched from iterration to recurrence
            SCCs.append(dfs(graph, vertex, explored))

    return SCCs
