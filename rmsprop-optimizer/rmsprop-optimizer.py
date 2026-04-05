import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    w, g, s = np.asarray(w), np.asarray(g), np.asarray(s)
    st = beta * s + (1 - beta) * g**2
    wt = w - lr / np.sqrt(st + eps) * g

    return (wt, st)