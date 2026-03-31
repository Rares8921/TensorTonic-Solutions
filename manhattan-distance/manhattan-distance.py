import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    return np.sum(np.absolute(np.asarray(x) - np.asarray(y))).astype(float)