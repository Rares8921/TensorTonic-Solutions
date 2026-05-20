def morphological_op(image, kernel, operation):
    """
    Apply morphological erosion or dilation to a binary image.
    """
    H, W = len(image), len(image[0])

    kh = len(kernel)
    kw = len(kernel[0])

    py = kh // 2
    px = kw // 2

    ans = [[0] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):

            if operation == "erode":
                value = 1

                for ki in range(kh):
                    for kj in range(kw):

                        if kernel[ki][kj] == 0:
                            continue

                        y = i + ki - py
                        x = j + kj - px

                        # zero padding
                        if not (0 <= y < H and 0 <= x < W):
                            value = 0
                            break

                        if image[y][x] == 0:
                            value = 0
                            break

                    if value == 0:
                        break

                ans[i][j] = value

            elif operation == "dilate":
                value = 0

                for ki in range(kh):
                    for kj in range(kw):

                        if kernel[ki][kj] == 0:
                            continue

                        y = i + ki - py
                        x = j + kj - px

                        # outside image = 0 because of zero padding
                        if 0 <= y < H and 0 <= x < W:
                            if image[y][x] == 1:
                                value = 1
                                break

                    if value == 1:
                        break

                ans[i][j] = value

    return ans