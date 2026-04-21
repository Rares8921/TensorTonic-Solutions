import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    y = np.asarray(y, dtype=int).ravel()

    if y.size == 0:
        raise ValueError("y must contain at least one label")
    if np.any(y < 0):
        raise ValueError("labels must be non-negative integers")

    if num_classes is None:
        num_classes = int(np.max(y)) + 1
    else:
        num_classes = int(num_classes)

    if num_classes < 1:
        raise ValueError("num_classes must be >= 1")
    if np.any(y >= num_classes):
        raise ValueError("labels must be < num_classes")

    n = y.shape[0]
    out = np.zeros((n, num_classes), dtype=float)
    out[np.arange(n), y] = 1.0

    return out