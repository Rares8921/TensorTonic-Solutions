import math

def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    n = len(actual_tokens)
    s = 0
    for i in range(n):
        s += math.log(prob_distributions[i][actual_tokens[i]])
    
    H = -s / n
    return math.exp(H)