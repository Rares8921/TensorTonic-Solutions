import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    try:
        A = np.asarray(matrix)
    except:
        return None
        
    if A.ndim != 2 or A.shape[0] != A.shape[1] or A.size == 0:
        return None

    eigvals = np.linalg.eigvals(A)

    return np.array( sorted(eigvals, key=lambda x:(x.real, x.imag)) )