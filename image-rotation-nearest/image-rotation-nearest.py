from math import radians, cos, sin

def rotate_image(image, angle_degrees):
    """
    Rotate the image counterclockwise by the given angle using nearest neighbor interpolation.
    """
    H, W = len(image), len(image[0])
    cy, cx = (H - 1) / 2, (W - 1) / 2
    theta = radians(angle_degrees)
    cs, sn = cos(theta), sin(theta)

    ans = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            dy, dx = i - cy, j - cx
            src_y = round(cy + dy * cs + dx * sn)
            src_x = round(cx - dy * sn + dx * cs)

            ans[i][j] = image[src_y][src_x]
    
    return ans