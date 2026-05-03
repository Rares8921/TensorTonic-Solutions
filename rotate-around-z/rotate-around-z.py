import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    points = np.asarray(points)
    flag = False 
    if points.ndim == 1:
        points = np.reshape(points, (1,3))
        flag = True

    cs, sn = np.cos(theta), np.sin(theta)
    
    ans = []
    for x, y, z in points:
        new_x = x * cs - y * sn
        new_y = x * sn + y * cs
        ans.append([new_x, new_y, z])

    return np.reshape(np.asarray(ans), (3,)) if flag else np.asarray(ans)