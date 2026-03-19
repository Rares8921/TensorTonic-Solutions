from math import log as ln

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    ans = []
    for i in range(len(y_true)):
        y = y_true[i]
        p = y_pred[i]
        p = min(max(p, eps), 1 - eps)
        
        log_loss = - (y * ln(p) + (1 - y) * ln(1 - p))
        ans.append(log_loss)

    return ans