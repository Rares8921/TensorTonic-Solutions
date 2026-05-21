import numpy as np

def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    series = np.asarray(series)
    n = series.shape[0]
    mean = np.mean(series)
    var = np.var(series)

    if var == 0.0:
        return [1] + [0] * max_lag

    ans = []
    for k in range(max_lag + 1):
        rk = sum([(series[t] - mean) * (series[t + k] - mean) for t in range(n - k)]) / var
        ans.append(np.float64(rk))

    norm_term = ans[0]
    for k in range(max_lag + 1):
        ans[k] /= norm_term
    
    return ans