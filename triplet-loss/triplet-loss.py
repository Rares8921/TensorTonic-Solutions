import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    a = np.atleast_2d(anchor).astype(float)
    p = np.atleast_2d(positive).astype(float)
    n = np.atleast_2d(negative).astype(float)

    d_ap = np.sum((a - p) ** 2, axis=1)
    d_an = np.sum((a - n) ** 2, axis=1)

    losses = np.maximum(0.0, d_ap - d_an + margin)

    return np.mean(losses)