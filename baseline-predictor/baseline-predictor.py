def baseline_predict(ratings_matrix, target_pairs):
    """
    Compute baseline predictions using global mean and user/item biases.
    """
    mu, cnt = 0, 0
    for line in ratings_matrix:
        for x in line:
            if x != 0:
                mu += x
                cnt += 1 
    mu /= cnt
    
    n = len(ratings_matrix)
    m = len(ratings_matrix[0])

    user_bias = [0.0] * n

    for u in range(n):
        total = 0
        cnt = 0

        for x in ratings_matrix[u]:
            if x != 0:
                total += x
                cnt += 1

        user_mean = total / cnt
        user_bias[u] = user_mean - mu

    # item biases
    item_bias = [0.0] * m

    for i in range(m):
        total = 0
        cnt = 0

        for u in range(n):
            if ratings_matrix[u][i] != 0:
                total += ratings_matrix[u][i]
                cnt += 1

        item_mean = total / cnt
        item_bias[i] = item_mean - mu

    # predictions
    result = []

    for u, i in target_pairs:
        pred = mu + user_bias[u] + item_bias[i]
        result.append(pred)

    return result