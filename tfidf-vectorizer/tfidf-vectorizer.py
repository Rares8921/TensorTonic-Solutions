import numpy as np
from collections import Counter, defaultdict
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    if not documents:
        return np.array([]), []

    tokenized_docs = [doc.lower().split() for doc in documents]
    vocab_set = set(word for doc in tokenized_docs for word in doc)
    vocabulary = sorted(vocab_set)
    
    vocab_index = {word: i for i, word in enumerate(vocabulary)}

    n_docs = len(documents)
    n_vocab = len(vocabulary)

    df_counts = defaultdict(int)
    for doc in tokenized_docs:
        unique_terms = set(doc)
        for term in unique_terms:
            df_counts[term] += 1

    idf_vector = np.zeros(n_vocab)
    for term, i in vocab_index.items():
        df_t = df_counts[term]
        idf_vector[i] = math.log(n_docs / df_t) if df_t else 0.0

    tfidf_matrix = np.zeros((n_docs, n_vocab))
    for doc_idx, doc in enumerate(tokenized_docs):
        term_counts = Counter(doc)
        total_terms = len(doc)
        for term, count in term_counts.items():
            i = vocab_index[term]
            tf = count / total_terms
            tfidf_matrix[doc_idx, i] = tf * idf_vector[i]

    return tfidf_matrix, vocabulary