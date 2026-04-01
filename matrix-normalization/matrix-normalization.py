import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    X = np.asarray(matrix)

    if X.ndim != 2:
        return None

    if norm_type == "l2":
        try:
            norm = np.sqrt(np.sum(X**2, axis=axis, keepdims=True))
        except:
            return None
    elif norm_type == "l1":
        try:
            norm = np.sum(np.abs(X), axis=axis, keepdims=True)
        except:
            return None
    elif norm_type == "max":
        try:
            norm = np.max(np.abs(X), axis=axis, keepdims=True)
        except:
            return None
    else:
        return None
        
    norm = np.where(norm == 0, 1, norm)

    return X / norm