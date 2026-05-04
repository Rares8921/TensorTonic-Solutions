def max_pooling_2d(X, p):
    """
    Apply 2D max pooling with non-overlapping windows.
    """
    # Write code here
    h, w = len(X), len(X[0])
    hout, wout = h // p, w // p

    ans = [[0 for _ in range(wout)] for _ in range(hout)]
    for i in range(hout):
        for j in range(wout):
            ans[i][j] = max([max([X[i * p + a][j * p + b] for b in range(p)]) for a in range(p)])

    return ans