def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    histogram = [0] * 256
    for row in image:
        for value in row:
            histogram[value] += 1

    return histogram