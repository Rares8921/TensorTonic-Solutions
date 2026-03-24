import numpy as np

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    x1, x2 = np.asarray(x1), np.asarray(x2)
    norm1, norm2 = np.linalg.norm(x1), np.linalg.norm(x2)
    cos = x1 @ x2 / (norm1 * norm2)

    print(cos)
    
    if label == 1:
        return 1 - cos
    
    return max(0, cos - margin)