def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    n = len(values)
    if n == 1:
        return [0.0]
        
    values_sorted = sorted(values)

    def _median(x, n):
        if n % 2 == 0:
            return (x[n // 2 - 1] + x[n // 2]) / 2

        return x[n // 2]

    median = _median(values_sorted, n)
    q1 = _median(values_sorted[:n//2], len(values_sorted[:n//2]))
    q3 = _median(values_sorted[n//2+n%2:], len(values_sorted[n//2+n%2:]))

    # avoid division by zero and keep the constraint of returning value - median
    if q1 == q3:
        q3 += 1

    iqr = q3 - q1

    ans = []
    for x in values:
        x_scaled = (x - median) / iqr
        ans.append(x_scaled)

    return ans