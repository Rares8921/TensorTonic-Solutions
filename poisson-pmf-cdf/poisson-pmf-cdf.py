import numpy as np
from math import factorial as fact

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    pmf = np.exp(-lam) * lam**k / fact(k)
    cdf = sum([np.exp(-lam) * lam**i / fact(i) for i in range(0, k + 1)])

    return (pmf, cdf)