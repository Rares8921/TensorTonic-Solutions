import numpy as np

def confusion_matrix_norm(y_true, y_pred, num_classes=None, normalize='none'):
    """
    Compute confusion matrix with optional normalization.
    """
    y_true = np.asarray(y_true, dtype=np.int64)
    y_pred = np.asarray(y_pred, dtype=np.int64)

    if y_true.shape != y_pred.shape:
        raise ValueError("y_true and y_pred must have the same shape")

    if num_classes is None:
        if y_true.size == 0:
            num_classes = 0
        else:
            num_classes = int(max(y_true.max(), y_pred.max()) + 1)

    if y_true.size:
        if (
            np.any(y_true < 0) or np.any(y_true >= num_classes) or
            np.any(y_pred < 0) or np.any(y_pred >= num_classes)
        ):
            raise ValueError("Labels must be in range [0, num_classes - 1]")

    cm = np.bincount(
        y_true * num_classes + y_pred,
        minlength=num_classes * num_classes
    ).reshape(num_classes, num_classes)

    if normalize == 'none':
        return cm

    cm = cm.astype(np.float64)
    eps = 1e-12

    if normalize == 'true':
        return cm / (cm.sum(axis=1, keepdims=True) + eps)

    if normalize == 'pred':
        return cm / (cm.sum(axis=0, keepdims=True) + eps)

    return cm / (cm.sum() + eps)