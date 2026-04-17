def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    return [sum(values[i:i+window_size]) / window_size for i in range(0, len(values) - window_size + 1)]