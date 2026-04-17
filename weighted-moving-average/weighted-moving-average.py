def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    ans = []
    
    w_sum = sum(weights)
    for i in range(0, len(values) - len(weights) + 1):
        s = sum(weights[j] * values[i + j] for j in range(len(weights)))
        ans.append(s / w_sum)

    return ans