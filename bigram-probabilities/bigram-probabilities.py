def bigram_probabilities(tokens):
    """
    Returns: (counts, probs)
      counts: dict mapping (w1, w2) -> integer count
      probs: dict mapping (w1, w2) -> float P(w2 | w1) with add-1 smoothing
    """
    from collections import defaultdict

    V = set(tokens)
    V_size = len(V)

    counts = defaultdict(int)
    for i in range(len(tokens) - 1):
        counts[(tokens[i], tokens[i + 1])] += 1

    context_counts = defaultdict(int)
    for (w1, w2), c in counts.items():
        context_counts[w1] += c

    probs = {}
    for w1 in V:
        for w2 in V:
            count_w1_w2 = counts.get((w1, w2), 0)
            total = context_counts.get(w1, 0)
            probs[(w1, w2)] = (count_w1_w2 + 1) / (total + V_size)

    return dict(counts), probs