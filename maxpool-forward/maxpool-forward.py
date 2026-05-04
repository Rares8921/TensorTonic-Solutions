def maxpool_forward(X, p, s):
    """
    Compute the forward pass of 2D max pooling.
    """
    h, w = len(X), len(X[0])
    hout = int((h - p) / s) + 1
    wout = int((w - p) / s) + 1

    ans = [[0 for _ in range(wout)] for _ in range(hout)]
    for i in range(hout):
        for j in range(wout):
            maximum = -100000000
            for a in range(p):
                for b in range(p):
                    maximum = max(maximum, X[i * s + a][j * s + b])
            ans[i][j] = maximum

    return ans