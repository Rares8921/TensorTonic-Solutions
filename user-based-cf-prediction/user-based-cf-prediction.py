def user_based_cf_prediction(similarities, ratings):
    """
    Predict a rating using user-based collaborative filtering.
    """
    denom = sum([s for s in similarities if s > 0])
    if denom == 0.0:
        return 0.0

    return sum([similarities[i] * ratings[i] for i in range(len(ratings)) if similarities[i] > 0]) / denom