import math

def adjusted_cosine_similarity(ratings_matrix, item_i, item_j):
    """
    Compute adjusted cosine similarity between two items.
    """
    numerator = 0.0
    denom_i = 0.0
    denom_j = 0.0

    for user_ratings in ratings_matrix:
        if user_ratings[item_i] != 0 and user_ratings[item_j] != 0:

            rated = [r for r in user_ratings if r != 0]
            mean_rating = sum(rated) / len(rated)

            diff_i = user_ratings[item_i] - mean_rating
            diff_j = user_ratings[item_j] - mean_rating

            numerator += diff_i * diff_j
            denom_i += diff_i ** 2
            denom_j += diff_j ** 2

    denominator = math.sqrt(denom_i) * math.sqrt(denom_j)

    if denominator == 0:
        return 0.0

    return numerator / denominator