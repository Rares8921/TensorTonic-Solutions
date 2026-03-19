import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    return 1 / len(y_pred) * sum([(y_pred[i] - y_true[i])**2 for i in range(len(y_pred))])
