import math

def bilinear_resize(image, new_h, new_w):
    """
    Resize a 2D grid using bilinear interpolation.
    """
    h = len(image)
    w = len(image[0])

    if h == new_h and w == new_w:
        return [[float(v) for v in row] for row in image]

    output = []

    for i in range(new_h):

        src_y = 0 if new_h == 1 else i * (h - 1) / (new_h - 1)

        y0 = int(math.floor(src_y))
        y1 = min(y0 + 1, h - 1)

        dy = src_y - y0

        row = []

        for j in range(new_w):

            src_x = 0 if new_w == 1 else j * (w - 1) / (new_w - 1)

            x0 = int(math.floor(src_x))
            x1 = min(x0 + 1, w - 1)

            dx = src_x - x0

            top_left = image[y0][x0]
            top_right = image[y0][x1]
            bottom_left = image[y1][x0]
            bottom_right = image[y1][x1]

            # Bilinear interpolation
            value = (
                top_left * (1 - dy) * (1 - dx) +
                bottom_left * dy * (1 - dx) +
                top_right * (1 - dy) * dx +
                bottom_right * dy * dx
            )

            row.append(value)

        output.append(row)

    return output