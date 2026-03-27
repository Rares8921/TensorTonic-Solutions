import numpy as np

def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    L = np.sqrt(6.0 / (fan_in + fan_out))
    return np.asarray(W) * (2 * L) - L