import numpy as np

def rolling_std(values, window_size):
    """
    Compute the rolling population standard deviation.
    """
    ans = []
    for i in range(len(values) - window_size + 1):
        windows = np.asarray(values[i:i+window_size])
        ans.append(float(np.std(windows)))

    return ans