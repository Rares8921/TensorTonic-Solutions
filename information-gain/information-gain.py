import numpy as np

def _entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    Use the _entropy() helper above.
    """
    # Write code here
    y = np.asarray(y)
    split_mask = np.asarray(split_mask, dtype=bool)

    H_parent = _entropy(y)

    left = y[split_mask]
    right = y[~split_mask]

    n = y.size
    nL = left.size
    nR = right.size

    if nL == 0 or nR == 0:
        return 0.0

    H_left = _entropy(left)
    H_right = _entropy(right)

    weighted = (nL / n) * H_left + (nR / n) * H_right

    return float(H_parent - weighted)