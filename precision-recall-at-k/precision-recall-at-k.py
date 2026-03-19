def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    relevant_set = set(relevant)
    precision, recall = 0.0, 0.0
    for i in range(k):
        if recommended[i] in relevant_set:
            precision += 1
            recall += 1

    precision /= k
    recall /= len(relevant)
    
    return [precision, recall]