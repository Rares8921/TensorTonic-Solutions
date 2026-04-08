def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    ans = []
    for i in range(0, len(values) - window_size + 1):
        v = sorted(values[i:i+window_size])
        n = len(v)
        if n % 2 == 0:
            median = (v[n//2 - 1] + v[n//2]) / 2
        else:
            median = v[n//2]

        ans.append(median)
    
    return ans