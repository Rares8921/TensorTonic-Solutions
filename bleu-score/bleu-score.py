def bleu_score(candidate, reference, max_n):
    """
    Compute the BLEU score for a candidate translation.
    """
    import math
    from collections import Counter
    
    if len(candidate) == 0:
        return 0.0
        
    c = len(candidate)
    r = len(reference)
    precisions = []

    for n in range(1, max_n + 1):
        cand_ngrams = [tuple(candidate[i:i+n]) for i in range(c - n + 1)]
        ref_ngrams = [tuple(reference[i:i+n]) for i in range(r - n + 1)]

        if len(cand_ngrams) == 0:
            return 0.0

        cand_counts = Counter(cand_ngrams)
        ref_counts = Counter(ref_ngrams)

        clipped = 0
        total = 0

        for ng, count in cand_counts.items():
            clipped += min(count, ref_counts.get(ng, 0))
            total += count

        p_n = clipped / total if total > 0 else 0.0
        if p_n == 0:
            return 0.0 

        precisions.append(p_n)

    log_sum = sum(math.log(p) for p in precisions)
    geo_mean = math.exp(log_sum / max_n)

    if c >= r:
        bp = 1.0
    else:
        bp = math.exp(1 - r / c)

    return bp * geo_mean