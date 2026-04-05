import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    w, g, G = np.asarray(w), np.asarray(g), np.asarray(G)
    Gt = G + g*g
    wt = w - lr / np.sqrt(Gt + eps) * g

    return (wt, Gt)