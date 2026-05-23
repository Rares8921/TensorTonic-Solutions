def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    bins = [[] for _ in range(n_bins)]

    # sample to bin
    for y, p in zip(y_true, y_pred):

        if p == 1.0:
            idx = n_bins - 1
        else:
            idx = int(p * n_bins)

        bins[idx].append((y, p))

    n = len(y_true)
    ece = 0.0

    for b in bins:

        if not b:
            continue

        bin_size = len(b)

        acc = sum(y for y, _ in b) / bin_size
        conf = sum(p for _, p in b) / bin_size

        ece += (bin_size / n) * abs(acc - conf)

    return ece