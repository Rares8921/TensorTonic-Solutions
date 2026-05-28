def gaussian_naive_bayes(X_train, y_train, X_test):
    """
    Predict class labels for test samples using Gaussian Naive Bayes.
    """
    epsilon = 1e-9
    classes = sorted(set(y_train))
    n_samples = len(X_train)
    n_features = len(X_train[0])

    priors = {}
    means = {}
    variances = {}

    for cls in classes:
        class_samples = [X_train[i] for i in range(n_samples) if y_train[i] == cls]

        class_count = len(class_samples)
        priors[cls] = class_count / n_samples

        class_means = []
        class_variances = []

        for feature_index in range(n_features):
            feature_values = [sample[feature_index] for sample in class_samples]

            mean = sum(feature_values) / class_count

            variance = sum((value - mean) ** 2 for value in feature_values) / class_count

            class_means.append(mean)
            class_variances.append(variance + epsilon)

        means[cls] = class_means
        variances[cls] = class_variances

    predictions = []

    for sample in X_test:
        best_class = None
        best_log_probability = float("-inf")

        for cls in classes:
            log_probability = math.log(priors[cls])

            for feature_index in range(n_features):
                mean = means[cls][feature_index]
                variance = variances[cls][feature_index]
                value = sample[feature_index]

                log_probability += (
                    -0.5 * math.log(2 * math.pi * variance)
                    - ((value - mean) ** 2) / (2 * variance)
                )

            if log_probability > best_log_probability:
                best_log_probability = log_probability
                best_class = cls

        predictions.append(best_class)

    return predictions