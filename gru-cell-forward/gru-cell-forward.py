import numpy as np

def _sigmoid(x):
    """Numerically stable sigmoid function"""
    return np.where(x >= 0, 1.0/(1.0+np.exp(-x)), np.exp(x)/(1.0+np.exp(x)))

def _as2d(a, feat):
    """Convert 1D array to 2D and track if conversion happened"""
    a = np.asarray(a, dtype=float)
    if a.ndim == 1:
        return a.reshape(1, feat), True
    return a, False

def gru_cell_forward(x, h_prev, params):
    """
    Implement the GRU forward pass for one time step.
    Supports shapes (D,) & (H,) or (N,D) & (N,H).
    """
    xt, x_was_1d = _as2d(x, params["Wz"].shape[0])
    h_prev, _ = _as2d(h_prev, params["Uz"].shape[0])
    
    Wz = np.asarray(params["Wz"])
    Wr = np.asarray(params["Wr"])
    Wh = np.asarray(params["Wh"])

    Uz = np.asarray(params["Uz"])
    Ur = np.asarray(params["Ur"])
    Uh = np.asarray(params["Uh"])

    bz = np.asarray(params["bz"])
    br = np.asarray(params["br"])
    bh = np.asarray(params["bh"])

    
    zt = _sigmoid(xt @ Wz + h_prev @ Uz + bz)
    rt = _sigmoid(xt @ Wr + h_prev @ Ur + br)
    ht_hat = np.tanh(xt @ Wh + (rt * h_prev) @ Uh + bh)
    ht = (1 - zt) * h_prev + zt * ht_hat

    if x_was_1d:
        return ht.reshape(-1)
        
    return ht