def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    ans = []
    for value in values:
        ans.append([value**deg for deg in range(0, degree + 1)])

    return ans