def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    total = {}
    for cat in categories:
        if cat in total:
            total[cat] += 1
        else:
            total[cat] = 1

    t = {}
    for i, cat in enumerate(categories):
        if cat in t:
            t[cat] += targets[i]
        else:
            t[cat] = targets[i]
            
    return [t[cat] / total[cat] for cat in categories]