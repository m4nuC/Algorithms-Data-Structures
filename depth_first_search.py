test_case = {
    1: [3, 2],
    2: [4],
    3: [1, 4, 5],
    4: [2, 3, 5, 6],
    5: [3, 4, 6],
    6: [4, 5]
}

test_case_3_components = {
    1: [5],
    2: [4],
    3: [5],
    4: [2],
    5: [1, 3, 7, 9],
    6: [8, 10],
    7: [5],
    8: [6, 10],
    9: [5],
    10: [6, 8]
}

test_case_dag = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}

test_case_dag_2 = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}

# algo have been change to take this format of input to allow reverse DFS
test_case = {
    1: [
        [],
        [2, 4]
    ],
    2: [
        [1],
        [3, 4]
    ],
    3: [
        [2, 4],
        []
    ],
    4: [
        [1, 2],
        [3]
    ]
}

def depth_first_search(G, start):
    stack = [start]
    explored = set([start])
    while(len(stack) > 0):
        current = stack.pop()
        print('looking at node:', current)
        next_candidates = G[current]
        for node in next_candidates:
            if node not in explored:
                stack.append(node)
                explored.add(node)
    return explored

def dfs(G, start, explored = set()):
    explored.add(start)
    for node in G[start][1]:
        if node not in explored:
            dfs(G, node, explored)
    return explored

def dfs_reverse(G, start, explored = set()):
    explored.add(start)
    print('reaching node:', start)
    print('explored :', explored)
    for node in G[start][0]:
        if node not in explored:
            dfs_reverse(G, node, explored)
    return explored