from constants import INF


def tsp(adjacency_matrix, src):
    n = len(adjacency_matrix)
    # table contains path weights from src to given node
    # table[i][j] contains path length from src to i containing nodes in j (binary form)
    table = [[INF for j in range(1 << n)] for i in range(n)]
    # initialize table for paths of length 2
    for i in range(n):
        table[i][(1 << src) | (1 << i)] = adjacency_matrix[src][i]

    def get_subsets(n, k):
        result = []

        def dfs(k, subset, start=0):
            if k == 0:
                result.append(subset)

            for i in range(start, n):
                if subset & (1 << i) == 0:
                    dfs(k - 1, subset | (1 << i), i + 1)

        dfs(k, 0)
        return result

    # solve for all path lengths
    for path_length in range(3, n + 1):
        for node_subset in get_subsets(n, path_length):
            if node_subset & (1 << src) == 0:
                continue

            for dst in range(n):
                if dst == src or node_subset & (1 << dst) == 0:
                    continue

                for end in range(n):
                    if end == src or end == dst or node_subset & (1 << end) == 0:
                        continue

                    table[dst][node_subset] = min(
                        table[dst][node_subset], table[end][node_subset ^ (1 << dst)] + adjacency_matrix[end][dst])

    # find optimal tour
    result = INF
    complete_subset = (1 << n) - 1
    for dst in range(n):
        if dst == src:
            continue

        result = min(
            result, table[dst][complete_subset] + adjacency_matrix[dst][src])

    return result


adjacency_matrix = [
    [0, 16, 11, 6],
    [8, 0, 13, 16],
    [4, 7, 0, 9],
    [5, 12, 2, 0],
]
print(tsp(adjacency_matrix, 0))
