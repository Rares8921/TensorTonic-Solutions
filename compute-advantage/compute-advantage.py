import numpy as np

def compute_advantage(states, rewards, V, gamma):
    """
    Returns: A (NumPy array of advantages)
    """
    states = np.asarray(states, dtype=int)
    rewards = np.asarray(rewards, dtype=int)
    V = np.asarray(V, dtype=float)

    n = len(rewards)
    G = np.zeros(n, dtype=float)

    G[-1] = rewards[-1]
    for t in range(n - 2, -1, -1):
        G[t] = rewards[t] + gamma * G[t + 1]
    
    return G - V[states]