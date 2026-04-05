import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    return np.percentile(np.asarray(x), np.asarray(q), method = 'linear')