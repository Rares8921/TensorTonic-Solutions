def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    N = len(values)
    min_val, max_val = min(values), max(values)
    if min_val == max_val:
        return [0] * N

    ans = []
    w = (max_val - min_val) / num_bins
    for val in values:
        bin = min(int((val - min_val) / w), num_bins - 1)
        ans.append(bin)

    return ans