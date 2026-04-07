import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    """
    Returns: V (NumPy array of shape (n_states,))
    """
    returns_sum = np.zeros(n_states)
    returns_count = np.zeros(n_states)

    for episode in episodes:
        G = 0
        states = [s for s, _ in episode]
        first_visit = {s: states.index(s) for s in set(states)}

        for t in reversed(range(len(episode))):
            state, reward = episode[t]
            G = reward + gamma * G

            if first_visit[state] == t:
                returns_sum[state] += G
                returns_count[state] += 1

    V = np.zeros(n_states)
    mask = returns_count > 0
    V[mask] = returns_sum[mask] / returns_count[mask]

    return V