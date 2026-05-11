def mean_rating_imputation(ratings_matrix, mode):
    """
    Fill missing ratings (zeros) with user or item means.
    """
    N, M = len(ratings_matrix), len(ratings_matrix[0])
    if mode == 'user':
        for i in range(N):
            mean, l = 0, 0
            for j in range(M):
                if ratings_matrix[i][j] != 0:
                    mean += ratings_matrix[i][j]
                    l += 1
            if l == 0:
                continue
            mean /= l
            for j in range(M):
                if ratings_matrix[i][j] == 0:
                    ratings_matrix[i][j] = mean
    else:
        for j in range(M):
            mean, l = 0, 0
            for i in range(N):
                if ratings_matrix[i][j] != 0:
                    mean += ratings_matrix[i][j]
                    l += 1
            if l == 0:
                continue
            mean /= l
            for i in range(N):
                if ratings_matrix[i][j] == 0:
                    ratings_matrix[i][j] = mean

    return ratings_matrix