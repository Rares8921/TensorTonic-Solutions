import numpy as np

def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    L = np.sqrt(6.0 / fan_in)
    return np.asarray(W) * (2 * L) - L