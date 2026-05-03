import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    points = np.asarray(points)
    T = np.asarray(T)

    def transform_point(p):
        p_h = np.hstack([p, 1.0])
        result = T @ p_h
        return result[:-1].tolist()

    if points.ndim == 1:
        return transform_point(points)

    return [transform_point(p) for p in points]