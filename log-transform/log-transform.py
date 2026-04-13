def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    from math import log
    ans = []
    for value in values:
        ans.append(log(1 + value))

    return ans