def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here
    v = []
    for i, score in enumerate(scores):
        if i not in rated_indices:
            v.append((score, i))

    v = sorted(v, key=lambda x: x[0], reverse=True)
    return [i for _, i in v[:k]]