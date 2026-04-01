import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.asarray(X)

    if X.ndim != 2 or X.shape[0] < 2:
        return None

    N = X.shape[0]
    mu = np.mean(X, axis=0)
    X_centered = X - mu

    cov = (X_centered.T @ X_centered) / (N - 1)
    return cov