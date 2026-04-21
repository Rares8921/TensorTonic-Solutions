import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    y_true = np.asarray(y_true).ravel()
    y_pred = np.asarray(y_pred).ravel()

    if y_true.shape[0] != y_pred.shape[0]:
        raise ValueError("y_true and y_pred must have same length")
    if y_true.size == 0:
        raise ValueError("inputs must be non-empty")

    labels = np.union1d(y_true, y_pred)
    n_classes = labels.size
    label_to_idx = {label: i for i, label in enumerate(labels)}

    # Confusion matrix
    cm = np.zeros((n_classes, n_classes), dtype=np.int64)
    ti = np.vectorize(label_to_idx.get)(y_true)
    pi = np.vectorize(label_to_idx.get)(y_pred)
    np.add.at(cm, (ti, pi), 1)

    total = cm.sum()
    accuracy = np.trace(cm) / total

    tp = np.diag(cm).astype(float)
    fp = cm.sum(axis=0) - tp
    fn = cm.sum(axis=1) - tp
    support = cm.sum(axis=1).astype(float)

    def safe_div(a, b):
        return np.divide(a, b, out=np.zeros_like(a, dtype=float), where=b != 0)

    prec = safe_div(tp, tp + fp)
    rec = safe_div(tp, tp + fn)
    f1 = safe_div(2 * prec * rec, prec + rec)

    if average == "micro":
        TP = tp.sum()
        FP = fp.sum()
        FN = fn.sum()

        precision = TP / (TP + FP) if (TP + FP) > 0 else 0.0
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0.0
        f1_score = (
            2 * precision * recall / (precision + recall)
            if (precision + recall) > 0 else 0.0
        )

    elif average == "macro":
        precision = prec.mean()
        recall = rec.mean()
        f1_score = f1.mean()

    elif average == "weighted":
        weights = support / support.sum()
        precision = np.sum(prec * weights)
        recall = np.sum(rec * weights)
        f1_score = np.sum(f1 * weights)

    elif average == "binary":
        if pos_label not in label_to_idx:
            raise ValueError("pos_label not found in labels")

        i = label_to_idx[pos_label]
        precision = prec[i]
        recall = rec[i]
        f1_score = f1[i]

    else:
        raise ValueError("average must be 'micro', 'macro', 'weighted', or 'binary'")

    return {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1_score),
    }