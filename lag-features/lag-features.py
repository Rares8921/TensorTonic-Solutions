def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    max_lag = max(lags)
    ans = []

    for t in range(max_lag, len(series)):
        ans.append([series[t - lag] for lag in lags])

    print(ans)
    return ans