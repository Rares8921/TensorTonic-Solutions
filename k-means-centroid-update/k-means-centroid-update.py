def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    points = [list(map(float, p)) for p in points]
    dim = len(points[0])

    sums = [[0.0] * dim for _ in range(k)]
    counts = [0] * k

    for p, c in zip(points, assignments):
        counts[c] += 1
        for d in range(dim):
            sums[c][d] += p[d]

    centroids = []
    for i in range(k):
        if counts[i] == 0:
            centroids.append([0.0] * dim)
        else:
            centroids.append([sums[i][d] / counts[i] for d in range(dim)])

    return centroids