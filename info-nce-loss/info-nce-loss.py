import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    # Write code here
    Z1 = np.asarray(Z1)
    Z2 = np.asarray(Z2)

    S = (Z1 @ Z2.T) / temperature
    S_stable = S - np.max(S, axis=1, keepdims=True)

    # exp and sum per row
    exp_S = np.exp(S_stable)
    sum_exp = np.sum(exp_S, axis=1)

    diag_exp = np.diag(exp_S)

    return np.mean(-np.log(diag_exp / sum_exp))