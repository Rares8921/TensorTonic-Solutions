def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    return [0.0 if series[i - 1] == 0 else (series[i] - series[i - 1]) / series[i - 1] for i in range(1, len(series))]