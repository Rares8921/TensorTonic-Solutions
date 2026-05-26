def gae(rewards, values, gamma, lam):
    """
    Compute Generalized Advantage Estimation.
    """
    T = len(rewards)
    ans = [0] * T
    for t in range(T - 1, -1, -1):
        delta = rewards[t] + gamma * values[t + 1] - values[t]
        if t == T - 1:
            ans[t] = delta
        else:
            ans[t] = delta + gamma * lam * ans[t + 1]

    return ans