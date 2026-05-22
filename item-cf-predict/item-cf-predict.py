def item_cf_predict(user_ratings, item_similarities, target):
    """
    Predict the rating using item-based collaborative filtering.
    """
    numerator = 0.0
    denominator = 0.0

    for i in range(len(user_ratings)):
        if i != target and item_similarities[i] > 0 and user_ratings[i] != 0:
            numerator += item_similarities[i] * user_ratings[i]
            denominator += item_similarities[i]

    if denominator == 0.0:
        return 0.0

    return numerator / denominator