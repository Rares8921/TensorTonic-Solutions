import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    return 1.0 / (1 + np.exp(-np.asarray(x, dtype=float)))