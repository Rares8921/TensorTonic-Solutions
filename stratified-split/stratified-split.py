import numpy as np

def stratified_split(X, y, test_size=0.2, rng=None):
    """
    Split features X and labels y into train/test while preserving class proportions.
    """
    X = np.asarray(X)
    y = np.asarray(y)

    if rng is None:
        rng = np.random.default_rng()

    train_idx = []
    test_idx = []

    for cls in np.unique(y):
        indices = np.flatnonzero(y == cls)

        shuffled = indices.copy()
        rng.shuffle(shuffled)

        n_class = len(indices)
        n_test = int(round(n_class * test_size))

        if n_class > 1:
            n_test = min(n_test, n_class - 1)

        test_idx.append(shuffled[:n_test])
        train_idx.append(shuffled[n_test:])

    train_idx = np.sort(np.concatenate(train_idx))
    test_idx = np.sort(np.concatenate(test_idx))

    return (
        X[train_idx],
        X[test_idx],
        y[train_idx],
        y[test_idx]
    )