import numpy as np

def clip_gradients(G, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    G = np.asarray(G)
    norm = np.linalg.norm(G)

    if max_norm <= 0 or norm == 0 or norm <= max_norm:
        return G.copy()

    return G * (max_norm / norm)