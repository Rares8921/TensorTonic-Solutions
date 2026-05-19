def robust_scaling(values):
    """
    Scale values using median and interquartile range (IQR).
    """
    if not values:
        return []

    if len(values) == 1:
        return [0.0]

    values_sorted = sorted(values)

    def median(seq):
        n = len(seq)
        mid = n // 2

        if n % 2 == 0:
            return (seq[mid - 1] + seq[mid]) / 2

        return seq[mid]

    n = len(values_sorted)
    mid = n // 2

    lower = values_sorted[:mid]
    upper = values_sorted[mid + n % 2:]

    med = median(values_sorted)
    q1 = median(lower)
    q3 = median(upper)

    iqr = q3 - q1

    if iqr == 0:
        return [x - med for x in values]

    return [(x - med) / iqr for x in values]