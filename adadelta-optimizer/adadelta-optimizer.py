import numpy as np

def adadelta_step(w, grad, E_grad_sq, E_update_sq, rho=0.9, eps=1e-6):
    """
    Perform one AdaDelta update step.
    """
    w, grad, E_grad_sq, E_update_sq = np.asarray(w), np.asarray(grad), np.asarray(E_grad_sq), np.asarray(E_update_sq)

    E_grad_sq_t = rho * E_grad_sq + (1 - rho) * grad**2
    
    delta_wt = -np.sqrt(E_update_sq + eps) / np.sqrt(E_grad_sq_t + eps) * grad
    
    E_update_sq_t = rho * E_update_sq + (1 - rho) * delta_wt**2

    wt = w + delta_wt

    return (wt, E_grad_sq_t, E_update_sq_t)