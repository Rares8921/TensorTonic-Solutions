import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    v = np.asarray(v)
    w = np.asarray(w)
    prod = np.linalg.norm(v) * np.linalg.norm(w)

    return np.arccos(v @ w / prod)