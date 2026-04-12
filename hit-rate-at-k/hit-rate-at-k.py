def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    cnt = 0
    N = len(recommendations)
    for i in range(N):
        valid = False
        for j in range(k):
            if recommendations[i][j] in ground_truth[i]:
                valid = True
                break

        if valid:
            cnt += 1

    return cnt / N