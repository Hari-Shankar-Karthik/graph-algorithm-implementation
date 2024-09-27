# AIM:
# Given a weighted DAG, find the shortest path from source node to destination
# For DAGs, this can be solved in linear time!

# ALGORITHM:
# Perform topological sort
# Make a distances array corresponding to the distances from the start node
# In order of the top sort, update distances

# COMPLEXITY:
# O(v + e) time
# O(v) space

# NOTE:
# For finding the longest path between two nodes in a weighted DAG,
# Flip the sign of each edge weight in the DAG and solve for shortest path :)
# For a general graph, finding longest path between two nodes is an NP-Hard problem
# Which means there does not exist a solution in polynomial time complexity

from collections import defaultdict

from constants import INF


# weighted_dag: map<T, list<tuple<T, int>>>
# src, dst: T
def dag_shortest_path(weighted_dag, src, dst):
    def topological_sort(weighted_dag):
        visited = set()
        result = []

        def dfs(node):
            visited.add(node)
            for next, edge_weight in weighted_dag[node]:
                if next not in visited:
                    dfs(next)

            result.append(node)

        for node in weighted_dag.keys():
            if node not in visited:
                dfs(node)

        result.reverse()
        return result

    distances = defaultdict(lambda: INF)
    distances[src] = 0
    prev_node = defaultdict(lambda: None)
    for node in topological_sort(weighted_dag):
        if node == dst:
            break

        for next, edge_wt in weighted_dag[node]:
            if distances[node] + edge_wt < distances[next]:
                distances[next] = distances[node] + edge_wt
                prev_node[next] = node

    curr_node = dst
    path = []
    while curr_node is not None:
        path.append(curr_node)
        curr_node = prev_node[curr_node]

    path.reverse()
    return path, distances[dst]


weighted_dag = {
    0: [(1, 3), (2, 6)],
    1: [(2, 4), (3, 4), (4, 11)],
    2: [(3, 8)],
    3: [(4, -4), (5, 5), (6, 2)],
    4: [(7, 9)],
    5: [(7, 1)],
    6: [(7, 2)],
    7: [],
}

print(dag_shortest_path(weighted_dag, 0, 7))
