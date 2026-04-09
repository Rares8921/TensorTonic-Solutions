def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    tmp = series
    while order > 0 and len(tmp) > 1:
        diff = []
        for i in range(len(tmp) - 1):
            diff.append(tmp[i + 1] - tmp[i])
            
        tmp = diff
        order -= 1

    return tmp