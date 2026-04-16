import numpy as np

def matrix_factorization_sgd_step(U, V, r, lr, reg):
    """
    Perform one SGD step for matrix factorization.
    """
    U = np.asarray(U)
    V = np.asarray(V)

    e = r - U @ V 
    U_new = U + lr * (e * V - reg * U)
    V_new = V + lr * (e * U - reg * V)

    return (U_new.tolist(), V_new.tolist())