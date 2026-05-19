def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    n, m = len(data), len(data[0])
    ans = [[0] * m for _ in range(n)]
    for j in range(m):
        mini, maxi = 1e9, -1e9
        for i in range(n):
            mini = min(mini, data[i][j])
            maxi = max(maxi, data[i][j])
        diff = maxi - mini
        if diff == 0:
            diff = 1

        for i in range(n):
            ans[i][j] = (data[i][j] - mini) / diff

    return ans