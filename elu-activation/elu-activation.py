import numpy as np

def elu(X, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    return [x if x > 0 else alpha * (np.exp(x) - 1) for x in X]