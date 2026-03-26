import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if seqs is None or len(seqs) == 0:
        return np.zeros((1, 1))
    # Your code here
    if max_len == None:
        max_len = 0
        for seq in seqs:
            max_len = max(max_len, len(seq))

    ans = []
    for seq in seqs:
        current = []
        for i in range(min(len(seq), max_len)):
            current.append(seq[i])

        while len(current) < max_len:
            current.append(pad_value)

        ans.append(current)

    return np.asarray(ans)