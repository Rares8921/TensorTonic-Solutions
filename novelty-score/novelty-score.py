from math import log2

def novelty_score(recommendations, item_counts, n_users):
    """
    Compute the average novelty of a recommendation list.
    """
    R = len(recommendations)
    if R == 0:
        return 0.0

    novelty = 0
    for i in range(R):
        ind = recommendations[i]
        novelty += -log2(item_counts[ind] / n_users)

    novelty /= R
    return novelty