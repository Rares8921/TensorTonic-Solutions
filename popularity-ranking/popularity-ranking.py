def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    ans = []
    for avg_rating, num_votes in items:
        term1 = (num_votes / (num_votes + min_votes)) * avg_rating
        term2 = (min_votes / (num_votes + min_votes)) * global_mean 
        wr = term1 + term2
        ans.append(wr)

    return ans