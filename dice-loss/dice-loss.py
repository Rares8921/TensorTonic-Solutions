import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here
    p = np.asarray(p, dtype=float)
    y = np.asarray(y, dtype=float)

    def dice(p, y):
        return (2 * np.sum(p*y) + eps) / (np.sum(p) + np.sum(y) + eps) 

    return 1 - dice(p, y)