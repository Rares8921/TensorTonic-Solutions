import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    t = np.asarray(x, dtype=float)
    return np.where(t >= 0, t, alpha * t)