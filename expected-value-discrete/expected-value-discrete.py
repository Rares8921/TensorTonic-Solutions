import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    p = np.asarray(p)
    if np.sum(p) < 1 - 1e-6:
        raise ValueError("probabilities must sum to 1")
        
    x = np.asarray(x)
    return np.sum(x * p)
