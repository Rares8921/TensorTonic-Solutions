from math import sqrt

def compute_monitoring_metrics(system_type, y_true, y_pred):
    """
    Compute the appropriate monitoring metrics for the given system type.
    """
    def safe_div(a, b):
        return a / b if b else 0.0

    metrics = {}

    if system_type == "classification":
        tp = fp = tn = fn = 0

        for yt, yp in zip(y_true, y_pred):
            if yt == 1 and yp == 1:
                tp += 1
            elif yt == 0 and yp == 1:
                fp += 1
            elif yt == 0 and yp == 0:
                tn += 1
            else:
                fn += 1

        n = len(y_true)

        accuracy = (tp + tn) / n
        precision = safe_div(tp, tp + fp)
        recall = safe_div(tp, tp + fn)
        f1 = safe_div(2 * precision * recall, precision + recall)

        metrics["accuracy"] = accuracy
        metrics["f1"] = f1
        metrics["precision"] = precision
        metrics["recall"] = recall

    elif system_type == "regression":
        n = len(y_true)

        mae = sum(abs(a - b) for a, b in zip(y_true, y_pred)) / n
        rmse = sqrt(sum((a - b) ** 2 for a, b in zip(y_true, y_pred)) / n)

        metrics["mae"] = mae
        metrics["rmse"] = rmse

    else:  
        order = sorted(range(len(y_pred)), key=lambda i: y_pred[i], reverse=True)
        top3 = order[:3]

        relevant_top3 = sum(y_true[i] for i in top3)
        total_relevant = sum(y_true)

        metrics["precision_at_3"] = relevant_top3 / 3
        metrics["recall_at_3"] = safe_div(relevant_top3, total_relevant)

    return sorted(metrics.items())