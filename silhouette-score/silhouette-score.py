import numpy as np

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.
    X: np.ndarray of shape (n_samples, n_features)
    labels: np.ndarray of shape (n_samples,)
    Returns: float
    """
    X = np.array(X)
    labels = np.array(labels)

    d = np.sqrt(((X[:, None] - X) ** 2).sum(axis=2))
    uniq = np.unique(labels)

    s = []

    for i in range(len(X)):
        same = labels == labels[i]
        same[i] = False

        a = d[i][same].mean() if same.sum() else 0

        b = min(
            d[i][labels == c].mean()
            for c in uniq if c != labels[i]
        )

        s.append((b - a) / max(a, b))

    return float(np.mean(s))