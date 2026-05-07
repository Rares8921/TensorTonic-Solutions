def gaussian_kernel(size, sigma):
    """
    Generate a normalized 2D Gaussian blur kernel.
    """
    if size == 1:
        return [[1.0]]
    
    center = size // 2
    kernel = []
    total = 0.0

    for i in range(size):
        row = []
        for j in range(size):
            x = j - center
            y = i - center

            value = math.exp(-(x * x + y * y) / (2 * sigma * sigma))
            row.append(value)
            total += value

        kernel.append(row)


    for i in range(size):
        for j in range(size):
            kernel[i][j] /= total

    return kernel