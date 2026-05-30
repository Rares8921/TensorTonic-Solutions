import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    X = np.asarray(X, dtype=float).copy()

    if X.ndim == 1:
        if strategy == 'mean':
            value = np.nanmean(X)
        else:
            value = np.nanmedian(X)

        if np.isnan(value):
            value = 0.0

        X[np.isnan(X)] = value
        return X

    if strategy == 'mean':
        values = np.nanmean(X, axis=0)
    else:
        values = np.nanmedian(X, axis=0)

    values = np.where(np.isnan(values), 0.0, values)

    rows, cols = np.where(np.isnan(X))
    X[rows, cols] = values[cols]

    return X