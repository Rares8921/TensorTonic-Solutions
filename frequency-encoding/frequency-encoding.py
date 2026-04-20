def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    from collections import Counter
    c = Counter(values)
    N = len(values)
    
    return [c[value] / N for value in values]