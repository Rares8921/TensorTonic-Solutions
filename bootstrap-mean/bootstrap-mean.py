import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    x = np.asarray(x, dtype=float)
    n = len(x)

    if rng is None:
        rng = np.random.default_rng()

    indices = rng.integers(0, n, size=(n_bootstrap, n))
    samples = x[indices]

    boot_means = np.mean(samples, axis=1)

    alpha = (1 - ci) / 2
    lower = np.quantile(boot_means, alpha)
    upper = np.quantile(boot_means, 1 - alpha)

    return boot_means, lower, upper