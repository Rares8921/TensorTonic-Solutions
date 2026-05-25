import numpy as np

def epsilon_greedy(q_values, epsilon, rng=None):
    """
    Returns: action index (int)
    """
    q_values = np.asarray(q_values)
    n = len(q_values)

    if rng is None:
        rand = np.random.random()
        if rand < epsilon:
            return int(np.random.randint(n))
        return int(np.argmax(q_values))
    else:
        if rng.random() < epsilon:
            return int(rng.integers(n))
        return int(np.argmax(q_values))
