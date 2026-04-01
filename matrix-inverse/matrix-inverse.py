import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    try:
        A = np.asarray(A, dtype=float)
    except:
        return None
    
    if A.ndim != 2 or A.shape[0] != A.shape[1] or A.size == 0 or np.linalg.det(A) == 0.0:
        return None
    
    return np.linalg.inv(A)