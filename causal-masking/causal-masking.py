import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions (e.g., -1e9)
    Return: masked scores (same shape, dtype=float)
    """
    scores = np.asarray(scores, dtype=float, copy=True)

    T = scores.shape[-1]
    
    mask = np.tril(np.ones((T, T), dtype=bool))

    scores[..., ~mask] = mask_value
    return scores