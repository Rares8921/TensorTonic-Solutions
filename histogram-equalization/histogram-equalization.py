def histogram_equalize(image):
    """
    Apply histogram equalization to enhance image contrast.
    """

    rows = len(image)
    cols = len(image[0])
    total_pixels = rows * cols

    # Build histogram
    hist = [0] * 256

    for row in image:
        for pixel in row:
            hist[pixel] += 1

    # Compute CDF
    cdf = [0] * 256
    cdf[0] = hist[0]

    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + hist[i]

    #Find cdf_min (smallest non-zero CDF value)
    cdf_min = 0

    for value in cdf:
        if value > 0:
            cdf_min = value
            break

    # all pixels identical
    if total_pixels == cdf_min:
        return [[0 for _ in row] for row in image]

    # Map pixels
    result = []

    for row in image:
        new_row = []

        for pixel in row:
            new_val = round(
                ((cdf[pixel] - cdf_min) /
                 (total_pixels - cdf_min)) * 255
            )

            new_row.append(new_val)

        result.append(new_row)

    return result