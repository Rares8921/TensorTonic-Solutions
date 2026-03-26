import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if y is None or len(y) == 0:
        return 0.0
        
    H = 0
    unique, counts = np.unique(y, return_counts=True)
    pi = [c / len(y) for c in counts]
    for p in pi:
        if p == 0:
            continue
        H += p * np.log2(p)

    return -H