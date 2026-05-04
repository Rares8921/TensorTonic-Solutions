def average_pooling_2d(X, p):
    """
    Apply 2D average pooling with non-overlapping windows.
    """
    h, w = len(X), len(X[0])
    hout, wout = h // p, w // p

    ans = [[0 for _ in range(wout)] for _ in range(hout)]
    CONST = 1/p**2
    for i in range(hout):
        for j in range(wout):
            ans[i][j] = CONST * (sum([sum([X[i * p + a][j * p + b] for b in range(p)]) for a in range(p)]))

    return ans