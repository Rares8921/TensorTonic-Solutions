def seasonal_average(series, period):
    """
    Compute the average value for each position in the seasonal cycle.
    """
    N = len(series)
    ans = []
    for p in range(period):
        step = 0
        s, l = 0, 0
        while p + step * period < N:
            s += series[p + step * period]
            l += 1
            step += 1

        ans.append(s / l)

    return ans