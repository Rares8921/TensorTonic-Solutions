def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    tp = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            tp += 1
            
    return tp / len(y_true)