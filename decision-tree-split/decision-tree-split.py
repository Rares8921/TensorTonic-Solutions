import numpy as np

def decision_tree_split(X, y):
    """
    Find the best feature and threshold to split the data.
    """
    X = np.array(X)
    y = np.array(y)

    def gini(labels):
        _, counts = np.unique(labels, return_counts=True)
        probabilities = counts / len(labels)
        return 1 - np.sum(probabilities ** 2)

    parent_gini = gini(y)

    best_gain = float("-inf")
    best_feature = -1
    best_threshold = None

    n_samples, n_features = X.shape

    for feature_index in range(n_features):
        values = np.sort(np.unique(X[:, feature_index]))

        for i in range(len(values) - 1):
            threshold = (values[i] + values[i + 1]) / 2

            left_mask = X[:, feature_index] <= threshold
            right_mask = X[:, feature_index] > threshold

            left_y = y[left_mask]
            right_y = y[right_mask]

            if len(left_y) == 0 or len(right_y) == 0:
                continue

            left_gini = gini(left_y)
            right_gini = gini(right_y)

            weighted_gini = (
                (len(left_y) / n_samples) * left_gini
                + (len(right_y) / n_samples) * right_gini
            )

            information_gain = parent_gini - weighted_gini

            if (
                information_gain > best_gain
                or (
                    information_gain == best_gain
                    and (
                        feature_index < best_feature
                        or (
                            feature_index == best_feature
                            and threshold < best_threshold
                        )
                    )
                )
            ):
                best_gain = information_gain
                best_feature = feature_index
                best_threshold = threshold

    return [best_feature, best_threshold]