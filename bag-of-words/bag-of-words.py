import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    freq = {}
    for token in tokens:
        if token not in freq:
            freq[token] = 1
        else:
            freq[token] += 1

    ans = []
    for word in vocab:
        if word in freq:
            ans.append(freq[word])
        else:
            ans.append(0)
        
    return np.asarray(ans, dtype=int)