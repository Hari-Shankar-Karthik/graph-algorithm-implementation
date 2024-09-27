# AIM:
# Using Dijkstra's algorithm as a single source shortest path (SSSP) algorithm
# Dijkstra's algorithm works on any graph which doesn't have any negative cycles
# (No problem with negative edge weights)

# ALGORITHM:
# Maintain an Indexed Priority Queue (IPQ) and a distances array
# Initialize the distance of source node to 0 and add it to the IPQ
# While the IPQ is non-is_empty, take out the node with the shortest distance from source
# Relax all its adjacent nodes, both in the array and in the IPQ
# When the IPQ is is_empty, return distances array

# NOTE:
# If you want to find the distance to a single destination, you can terminate early
# In the while loop, break immediately when you see destination node

# COMPLEXITY:
# O((e + v) * log(v)) time
# O(v) space

from collections import defaultdict

from constants import INF


class IndexedPriorityQueue:
    def __init__(self):
        self.heap = []

    def get_parent(self, child):
        return (child - 1) // 2

    def get_first_child(self, parent):
        return 2 * parent + 1

    def sift_up(self, child):
        parent = self.get_parent(child)
        while parent >= 0 and self.heap[parent][1] > self.heap[child][1]:
            self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
            child = parent
            parent = self.get_parent(child)

    def sift_down(self, parent):
        child = self.get_first_child(parent)
        n = len(self.heap)
        while child < n:
            if child + 1 < n and self.heap[child + 1][1] < self.heap[child][1]:
                child += 1

            if self.heap[child][1] >= self.heap[parent][1]:
                break

            self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            parent = child
            child = self.get_first_child(parent)

    def upsert(self, key, value):
        i = 0
        n = len(self.heap)
        while i < n and self.heap[i][0] != key:
            i += 1

        if i >= n:
            self.heap.append([key, value])
            self.sift_up(n)
        else:
            self.heap[i][1] = value
            self.sift_up(i)

    def is_empty(self):
        return not self.heap

    def pop(self):
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.sift_down(0)
        return result


# weighted_adj_list: map<T, list<tuple<T, int>>>
# src: T
def dijkstra_sssp(weigthed_adj_list, src):
    distances = defaultdict(lambda: INF)
    distances[src] = 0
    ipq = IndexedPriorityQueue()
    ipq.upsert(src, 0)
    while not ipq.is_empty():
        node, dist = ipq.pop()
        for next, edge_wt in weigthed_adj_list[node]:
            if dist + edge_wt < distances[next]:
                distances[next] = dist + edge_wt
                ipq.upsert(next, distances[next])

    return distances

# weighted_adj_list: map<T, list<tuple<T, int>>>
# src, dst: T


def dijkstra_between(weighted_adj_list, src, dst):
    distances = defaultdict(lambda: INF)
    distances[src] = 0
    ipq = IndexedPriorityQueue()
    ipq.upsert(src, 0)
    prev_node = defaultdict(lambda: None)
    while not ipq.is_empty():
        node, dist = ipq.pop()
        if node == dst:
            break

        for next, edge_wt in weighted_adj_list[node]:
            if dist + edge_wt < distances[next]:
                prev_node[next] = node
                distances[next] = dist + edge_wt
                ipq.upsert(next, distances[next])

    if dst not in distances:
        return INF

    path = []
    node = dst
    while node is not None:
        path.append(node)
        node = prev_node[node]

    path.reverse()
    return path, distances[dst]


weighted_adj_list = {
    0: [(1, 7), (2, 9), (5, 14)],
    1: [(0, 7), (2, 10), (3, 15)],
    2: [(0, 9), (1, 10), (3, 11), (5, 2)],
    3: [(1, 15), (2, 11), (4, 6)],
    4: [(3, 6), (5, 9)],
    5: [(0, 14), (2, 2), (4, 9)],
    6: [(7, 2), (8, 1)],
    7: [(6, 2), (8, 7)],
    8: [(6, 1), (7, 7), (9, 3)],
    9: [(8, 3)],
}
print(dijkstra_between(weighted_adj_list, 0, 7))
