import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    C = np.asarray(C)
    total = np.sum(C)
    E = (np.sum(C, axis=1, keepdims=True) @ np.sum(C, axis=0, keepdims=True)) / total
    return (np.sum((C - E) ** 2 / E), E)