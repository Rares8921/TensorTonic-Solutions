import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    y_left = np.asarray(y_left)
    y_right = np.asarray(y_right)

    NL = len(y_left)
    NR = len(y_right)
    N = NL + NR

    if N == 0:
        return 0.0

    def gini(y):
        if len(y) == 0:
            return 0.0
        _, counts = np.unique(y, return_counts=True)
        probs = counts / counts.sum()
        return 1.0 - np.sum(probs ** 2)

    gini_left = gini(y_left)
    gini_right = gini(y_right)

    return (NL / N) * gini_left + (NR / N) * gini_right