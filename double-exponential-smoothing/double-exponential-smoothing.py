def double_exponential_smoothing(series, alpha, beta):
    """
    Apply Holt's linear trend method and return the level values.
    """
    # Write code here
    l = series[0]
    t = series[1] - series[0]
    N = len(series)
    ans = [l]
    for i in range(1, N):
        lt = alpha * series[i] + (1 - alpha) * (l + t)
        tt = beta * (lt - l) + (1 - beta) * t

        l = lt
        t = tt
        ans.append(l)
    
    return ans