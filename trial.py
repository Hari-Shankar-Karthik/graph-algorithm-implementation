def get_subsets(n, k):
    result = []

    def dfs(k, subset, start=0):
        print(f'dfs({k}, {subset}, {start})')
        if k == 0:
            result.append(subset)

        for i in range(start, n):
            if subset & (1 << i) == 0:
                dfs(k - 1, subset | (1 << i), i + 1)

    dfs(k, 0)
    return result


print(get_subsets(4, 3))
