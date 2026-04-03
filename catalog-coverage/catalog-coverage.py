def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    return len(set(sum(recommendations, []))) / n_items