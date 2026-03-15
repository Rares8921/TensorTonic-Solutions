def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    ans = []
    for row in image:
        current = []
        for pixel in row:
            r, g, b = pixel
            current.append(0.299 * r + 0.587 * g + 0.114 * b)
        
        ans.append(current)

    return ans