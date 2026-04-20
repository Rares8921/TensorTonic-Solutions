def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    mp = {}
    for i, order in enumerate(ordering):
        mp[order] = i

    return [mp[value] for value in values]