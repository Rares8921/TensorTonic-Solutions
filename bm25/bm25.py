import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    """
    Returns numpy array of BM25 scores for each document.
    """
    N = len(docs)
    if N == 0:
        return np.array([], dtype=float)

    doc_lens = np.array([len(doc) for doc in docs], dtype=float)
    avgdl = doc_lens.mean() if N > 0 else 0.0

    # doc freq for each term in query
    df = {}
    for t in set(query_tokens):
        df[t] = sum(1 for doc in docs if t in doc)

    # idf for each query term
    idf = {}
    for t in query_tokens:
        df_t = df.get(t, 0)
        if df_t == 0:
            idf[t] = 0.0
        else:
            idf[t] = math.log((N - df_t + 0.5) / (df_t + 0.5) + 1)

    # now scores
    scores = np.zeros(N, dtype=float)
    for i, doc in enumerate(docs):
        tf_counter = Counter(doc)
        D_len = doc_lens[i]
        for t in query_tokens:
            tf = tf_counter.get(t, 0)
            if tf == 0:
                continue
            denom = tf + k1 * (1 - b + b * D_len / avgdl)
            numer = tf * (k1 + 1)
            scores[i] += idf[t] * numer / denom

    return scores