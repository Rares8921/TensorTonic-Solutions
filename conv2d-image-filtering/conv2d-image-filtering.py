def conv2d(image, kernel, stride=1, padding=0):
    """
    Apply 2D convolution to a single-channel image.
    """
    h, w = len(image), len(image[0])
    kh, kw = len(kernel), len(kernel[0])

    # Create padded image
    padded_h = h + 2 * padding
    padded_w = w + 2 * padding

    padded = [[0] * padded_w for _ in range(padded_h)]

    for i in range(h):
        for j in range(w):
            padded[i + padding][j + padding] = image[i][j]

    # Compute output dimensions
    out_h = ((h + 2 * padding - kh) // stride) + 1
    out_w = ((w + 2 * padding - kw) // stride) + 1

    output = [[0.0 for _ in range(out_w)] for _ in range(out_h)]

    # Perform convolution
    for i in range(out_h):
        for j in range(out_w):
            total = 0.0

            for m in range(kh):
                for n in range(kw):
                    total += (
                        padded[i * stride + m][j * stride + n]
                        * kernel[m][n]
                    )

            output[i][j] = total

    return output