import numpy as np

def mean_average_precision(y_true_list, y_score_list, k=None):
    """
    Compute Mean Average Precision (mAP) for multiple retrieval queries.
    """
    ap_per_query = []

    for y_true, y_score in zip(y_true_list, y_score_list):
        y_true = np.asarray(y_true, dtype=np.int8)
        y_score = np.asarray(y_score, dtype=np.float64)

        order = np.argsort(-y_score)
        y_true = y_true[order]

        total_relevant = int(y_true.sum())

        if total_relevant == 0:
            ap_per_query.append(0.0)
            continue

        if k is not None:
            y_true = y_true[:k]

        cumulative_relevant = np.cumsum(y_true)
        ranks = np.arange(1, len(y_true) + 1)

        precision = cumulative_relevant / ranks
        ap = np.sum(precision * y_true) / total_relevant

        ap_per_query.append(float(ap))

    map_value = float(np.mean(ap_per_query)) if ap_per_query else 0.0

    return map_value, ap_per_query