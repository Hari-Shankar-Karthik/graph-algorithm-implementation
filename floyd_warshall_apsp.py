# AIM:
# To find the distances of every node from one another using Floyd-Warshall's Algorithm
# Floyd-Warshalls's Algorithm works on small weighted graphs with negative cycles too

# ALGORITHM:
# Initialize the dp table as n x n matrix
# dp table should contain the distances between each node pair
# Then, iterate over every 'unlocked_vertex':
# For evert node pair, relax path length using unlocked_vertex
# Rerun again, if further relaxation possible, set distance as -INFinity

# COMPLEXITY:
# O(v^3) time
# O(v^2) space

# adjacency_matrix: list<list<int>>
from constants import INF


def floyd_warshall_apsp(adjacency_matrix):
    node_count = len(adjacency_matrix)
    table = [[INF for j in range(node_count)] for i in range(node_count)]
    for i in range(node_count):
        for j in range(node_count):
            table[i][j] = adjacency_matrix[i][j]

    for k in range(node_count):
        for i in range(node_count):
            for j in range(node_count):
                table[i][j] = min(table[i][j], table[i][k] + table[k][j])

    for k in range(node_count):
        for i in range(node_count):
            for j in range(node_count):
                if table[i][k] + table[k][j] < table[i][j]:
                    table[i][j] = -INF

    return table


adjacency_matrix = [
    [0, 1, 1, INF, INF, INF, INF, INF, INF, INF],
    [INF, 0, INF, 2, INF, INF, INF, INF, INF, INF],
    [INF, 1, 0, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, 6, 0, 3, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, 0, 1, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, 0, 1, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, 0, 2, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, 0, 1, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, 0, 3],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0]
]
print(floyd_warshall_apsp(adjacency_matrix))
