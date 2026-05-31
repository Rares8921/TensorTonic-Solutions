import numpy as np

def kfold_split(N, k, shuffle=True, rng=None):
    """
    Returns: list of length k with tuples (train_idx, val_idx)
    """
    idx = np.arange(N)

    if shuffle:
        if rng is not None:
            idx = rng.permutation(idx)
        else:
            np.random.shuffle(idx)

    base_size = N // k
    remainder = N % k

    fold_sizes = np.full(k, base_size, dtype=int)
    fold_sizes[:remainder] += 1

    folds = []
    start = 0

    for size in fold_sizes:
        end = start + size
        folds.append(idx[start:end])
        start = end

    result = []

    for i in range(k):
        val_idx = folds[i]
        train_idx = np.concatenate(folds[:i] + folds[i + 1:])

        result.append(
            (
                train_idx.astype(int),
                val_idx.astype(int)
            )
        )

    return result