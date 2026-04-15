import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    fpr = np.asarray(fpr)
    tpr = np.asarray(tpr)

    if fpr.shape != tpr.shape or len(fpr) < 2:
        raise ValueError("")

    return np.sum((fpr[1:] - fpr[:-1]) * (tpr[1:] + tpr[:-1]) / 2.0)