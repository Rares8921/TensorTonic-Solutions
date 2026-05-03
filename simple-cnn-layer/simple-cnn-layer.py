import numpy as np

def conv2d(x, w, b):
    """
    Simple 2D convolution layer forward pass.
    Valid padding, stride=1.
    """
    N, C_in, H, W = x.shape
    C_out, _, KH, KW = w.shape

    H_out = H - KH + 1 
    W_out = W - KW + 1

    y = np.zeros((N, C_out, H_out, W_out), dtype=float)

    for n in range(N):
        for cout in range(C_out):
            for i in range(H_out):
                for j in range(W_out):
                    patch = x[n, :, i:i+KH, j:j+KW]
                    y[n, cout, i, j] = np.sum(patch * w[cout]) + b[cout]
    
    return y