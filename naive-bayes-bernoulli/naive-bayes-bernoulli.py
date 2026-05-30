import numpy as np

def naive_bayes_bernoulli(X_train, y_train, X_test):
    """
    Compute log-likelihood P(y|x) for Bernoulli Naive Bayes.
    """
    X_train = np.asarray(X_train, dtype=np.float64)
    y_train = np.asarray(y_train)
    X_test = np.asarray(X_test, dtype=np.float64)

    classes = np.sort(np.unique(y_train))
    n_samples = len(y_train)

    log_posteriors = []

    for cls in classes:
        mask = y_train == cls
        X_cls = X_train[mask]

        prior = X_cls.shape[0] / n_samples
        log_prior = np.log(prior)

        theta = (X_cls.sum(axis=0) + 1) / (X_cls.shape[0] + 2)

        log_likelihood = (
            X_test * np.log(theta) +
            (1 - X_test) * np.log(1 - theta)
        ).sum(axis=1)

        log_posteriors.append(log_prior + log_likelihood)

    return np.column_stack(log_posteriors)