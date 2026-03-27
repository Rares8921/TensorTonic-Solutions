import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    x = np.asarray(x)
    gamma = np.asarray(gamma)
    beta = np.asarray(beta)

    if x.ndim == 2:
        mu = np.mean(x, axis=0)
        var = np.var(x, axis=0)
    else:
        mu = np.mean(x, axis=(0, 2, 3), keepdims=True)
        var = np.var(x, axis=(0, 2, 3), keepdims=True)

        gamma = gamma.reshape(1, -1, 1, 1)
        beta = beta.reshape(1, -1, 1, 1)

    x_hat = (x - mu) / np.sqrt(var + eps)
    out = gamma * x_hat + beta
    return out
        