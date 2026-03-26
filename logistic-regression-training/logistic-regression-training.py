import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)

    N, D = X.shape
    
    w, b, = np.zeros(D), 0.0
    for _ in range(steps):
        p = _sigmoid(X @ w + b)
        py = p - y
        dw = (X.T @ py) / N
        db = np.mean(py)

        w = w - lr * dw
        b = b - lr * db
    
    return (w, b)