import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    x = np.asarray(x, dtype=float)
    m = np.mean(x)
    n = x.shape[0]

    s = np.sqrt(np.sum((x - m)**2) / (n - 1))

    return (m - mu0) / (s / np.sqrt(n))