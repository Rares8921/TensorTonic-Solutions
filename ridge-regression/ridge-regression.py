import numpy as np

def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    X = np.asarray(X)
    y = np.asarray(y)
    prod = X.T @ X 
    I = np.identity(prod.shape[0])
    
    W = np.linalg.inv(prod + lam * I) @ X.T @ y

    return W