def sobel_edges(image):
    """
    Apply the Sobel operator to detect edges.
    """
    # Write code here
    Kx = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]

    Ky = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ]

    n, m = len(image), len(image[0])
    padded = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(m):
            padded[i + 1][j + 1] = image[i][j]

    ans = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            gx = 0
            gy = 0

            for x in range(3):
                for y in range(3):
                    val = padded[i + x][j + y]
                    gx += val * Kx[x][y]
                    gy += val * Ky[x][y]

            ans[i][j] = math.sqrt(gx * gx + gy * gy)

    return ans