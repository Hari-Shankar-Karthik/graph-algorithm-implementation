# AIM:
# Given a directed acyclic graph (DAG), create a topological sort for it
# A topological sort is a total ordering of the nodes of the graph
# It respects the partial ordering between nodes as described by the DAG

# ALGORITHM:
# For every node in the graph, perform dfs starting from it (if it is unvisited)
# While returning from dfs, add this node to the front of the top sort

# COMPLEXITY:
# O(v + e) time
# O(v) space

# dag: map<T, list<T>> (adjacency list)
def topological_sort(dag):
    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        for next in dag[node]:
            if next not in visited:
                dfs(next)

        result.append(node)
        # ideally we should add at the beginning
        # we will reverse the result before returning it

    for node in dag.keys():
        if node not in visited:
            dfs(node)

    result.reverse()
    return result


dag = {
    'A': ['B', 'D'],
    'B': ['E'],
    'C': ['F'],
    'D': ['E', 'F'],
    'E': ['G', 'H'],
    'F': ['G', 'I'],
    'G': ['J', 'I'],
    'H': ['J'],
    'I': [],
    'J': [],
    'K': [],
}

print(topological_sort(dag))
