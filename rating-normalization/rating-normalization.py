import numpy as np

def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    M = np.array(matrix, dtype=float)

    mask = M != 0

    sums = M.sum(axis=1)
    counts = mask.sum(axis=1)

    means = np.divide(sums, counts, out=np.zeros_like(sums), where=counts!=0)

    normalized = np.where(mask, M - means[:, None], 0.0)

    return normalized.tolist()