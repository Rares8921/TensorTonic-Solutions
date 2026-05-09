import numpy as np

def knn_distance(X_train, X_test, k):
    """
    Compute pairwise distances and return k nearest neighbor indices.
    """
    X_train = np.asarray(X_train)
    X_test = np.asarray(X_test)

    if X_train.ndim == 1:
        X_train = X_train.reshape(-1, 1)
    if X_test.ndim == 1:
        X_test = X_test.reshape(-1, 1)

    diff = X_test[:, None, :] - X_train[None, :, :]
    dist = np.sum(diff * diff, axis=2)

    n_train = X_train.shape[0]
    k_eff = min(k, n_train)

    idx = np.argsort(dist, axis=1)[:, :k_eff]

    if k_eff < k:
        pad = np.full((X_test.shape[0], k - k_eff), -1, dtype=int)
        idx = np.concatenate([idx, pad], axis=1)

    return idx.astype(int)