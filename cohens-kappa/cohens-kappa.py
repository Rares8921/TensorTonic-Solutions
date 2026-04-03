from collections import Counter

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    n = len(rater1)
    
    labels = set(rater1).union(set(rater2))
    cnt1 = Counter(rater1)
    cnt2 = Counter(rater2)
    pe = 0
    for label in labels:
        if label in cnt1:
            c1 = cnt1[label]
        else:
            c1 = 0

        if label in cnt2:
            c2 = cnt2[label]
        else:
            c2 = 0

        pe += c1 * c2 / n**2

    if pe == 1.0:
        return 1.0
    
    po = len([1 for i in range(n) if rater1[i] == rater2[i]]) / n

    print(po, pe)
    return (po - pe) / (1 - pe)