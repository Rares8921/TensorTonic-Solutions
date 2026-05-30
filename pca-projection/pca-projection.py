import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    X = np.array(X, dtype=float)

    X_centered = X - np.mean(X, axis=0)

    covariance = (X_centered.T @ X_centered) / (X.shape[0] - 1)

    eigenvalues, eigenvectors = np.linalg.eigh(covariance)

    indices = np.argsort(eigenvalues)[::-1][:k]
    principal_components = eigenvectors[:, indices]

    return (X_centered @ principal_components).tolist()