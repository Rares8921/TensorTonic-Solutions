def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    K = len(predictions)
    q = [(1 - epsilon if i == target else 0) + epsilon / K for i in range(K)]

    from math import log
    return -sum([q[i] * log(predictions[i]) for i in range(K)])