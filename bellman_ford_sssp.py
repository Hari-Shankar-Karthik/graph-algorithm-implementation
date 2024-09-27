# AIM:
# To find the distances of every node from a given node using Bellman-Ford's Algorithm
# Bellman-Ford's Algorithm works on weighted graphs with negative cycles too

# ALGORITHM:
# If we assume that there aren't any negative cycles,
# It would take atmost (v - 1) turns for every distance to propagate along all edges
# If there are negative cycles, they will propagate in another (v - 1) turns

# PSEUDOCODE:
# Repeat (v - 1) times:
# For every edge in the graph, relax the distance to the destination
# Repeat (v - 1) times:
# If possible to relax an edge, set distance to destination to -infinity

# COMPLEXITY:
# O(v * e) time
# O(v) space


from collections import defaultdict

from constants import INF

# weighted_edge_list: list<tuple<T, T, int>>
# src: T


def bellman_ford_sssp(num_vertices, weighted_edge_list, src):
    distances = defaultdict(lambda: INF)
    distances[src] = 0
    for _ in range(num_vertices - 1):
        for v1, v2, edge_wt in weighted_edge_list:
            distances[v2] = min(distances[v2], distances[v1] + edge_wt)

    for _ in range(num_vertices - 1):
        for v1, v2, edge_wt in weighted_edge_list:
            if distances[v1] + edge_wt < distances[v2]:
                distances[v2] = -INF

    return distances


weighted_edge_list = [(0, 1, 1), (0, 2, 1), (2, 1, 1), (1, 3, 4),
                      (3, 2, -6), (3, 4, 1), (3, 5, 1), (4, 5, 1), (4, 6, 1), (5, 6, 1)]
print(bellman_ford_sssp(7, weighted_edge_list, 3))
