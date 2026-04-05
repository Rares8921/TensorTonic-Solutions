def priority_replay_sample(priorities, alpha, beta):
    """
    Compute sampling probabilities and importance sampling weights for PER.
    """
    N = len(priorities)
    priorities = [p**alpha for p in priorities]
    denom = sum(priorities)
    probs, w = [], []
    for p in priorities:
        pi = p / denom
        probs.append(pi)
        
        wi = (N * pi)**(-beta)
        w.append(wi)

    w_max = max(w)
    for i in range(N):
        w[i] /= w_max

    return [probs, w]
    