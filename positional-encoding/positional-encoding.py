import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    if seq_len < 1 or d_model < 1:
        return None

    # Positions: (seq_len, 1)
    pos = np.arange(seq_len)[:, np.newaxis]

    # Dimension indices: (d_model,)
    i = np.arange(d_model)

    # Compute the divisor term
    denom = base ** (2 * (i // 2) / d_model)
    
    # Compute angles
    angles = pos / denom
    
    # Initialize output
    PE = np.zeros((seq_len, d_model), dtype=float)
    
    # Apply sin to even indices, cos to odd
    PE[:, 0::2] = np.sin(angles[:, 0::2])
    PE[:, 1::2] = np.cos(angles[:, 1::2])
    
    return PE