import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    X = np.asarray(X, dtype=float)

    if X.ndim != 2 or X.shape[0] < 2:
        return None

    N = X.shape[0]
    mu = np.mean(X, axis=0)
    X_centered = X - mu

    cov = (X_centered.T @ X_centered) / (N - 1)
    std = np.sqrt(np.diag(cov))
    denom = np.outer(std, std)

    with np.errstate(divide='ignore', invalid='ignore'):
        corr = cov / denom
    corr[denom == 0] = np.nan

    return corr