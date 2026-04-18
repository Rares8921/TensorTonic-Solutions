def discount_returns(rewards, gamma):
    """
    Compute the discounted return at every timestep.
    """
    # Write code here
    N = len(rewards)
    G = [0] * N
    G[-1] = rewards[-1]
    for t in range(N - 2, -1, -1):
        G[t] = rewards[t] + gamma * G[t + 1]
    
    return G