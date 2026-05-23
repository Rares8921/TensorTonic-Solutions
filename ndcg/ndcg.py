import math

def dcg(scores, k):
    k = min(k, len(scores))
    total = 0.0

    for i in range(k):

        rel = scores[i]

        gain = (2 ** rel) - 1
        discount = math.log2(i + 2)

        total += gain / discount

    return total

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    actual_dcg = dcg(relevance_scores, k)

    ideal_scores = sorted(relevance_scores, reverse=True)
    ideal_dcg = dcg(ideal_scores, k)

    if ideal_dcg == 0:
        return 0.0

    return actual_dcg / ideal_dcg