import numpy as np

def td_value_update(V, s, r, s_next, alpha, gamma):
    """
    Returns: updated value function V_new
    """
    V_new = np.asarray(V, dtype=float).copy()
    
    delta = r + gamma * V_new[s_next] - V_new[s]
    V_new[s] += alpha * delta

    return V_new