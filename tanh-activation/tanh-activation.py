import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x = np.asarray(x)
    e1, e2 = np.exp(x), np.exp(-x)
    return (e1 - e2) / (e1 + e2)