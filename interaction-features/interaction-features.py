def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here
    for k in range(len(X)):
        features = list(X[k])
        for i in range(len(X[k]) - 1):
            for j in range(i + 1, len(X[k])):
                features.append(X[k][i] * X[k][j])

        X[k] = features

    return X