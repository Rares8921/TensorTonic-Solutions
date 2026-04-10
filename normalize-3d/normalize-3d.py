import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v = np.asarray(v, dtype=float)
    if v.ndim == 1:
        v = v.reshape(1, 3)

    norms = np.linalg.norm(v, axis=1, keepdims=True)
    norms = np.where(norms > 1e-10, norms, 1.0)

    normalized = v / norms
    normalized = np.where(norms > 1e-10, normalized, 0.0)
    
    return normalized[0] if v.shape == (1, 3) else normalized