def _dot(a, b):
    """Dot product of two vectors."""
    return sum(x * y for x, y in zip(a, b))

def lbfgs_direction(grad, s_list, y_list):
    """
    Compute the L-BFGS search direction using the two-loop recursion.
    """
    # Write code here
    q = grad[:]
    rho = [1 / _dot(y, s) for s, y in zip(s_list, y_list)]
    alpha = [0.0] * len(s_list)

    for i in range(len(s_list) - 1, -1, -1):
        alpha[i] = rho[i] * _dot(s_list[i], q)
        q = [a - alpha[i] * b for a, b in zip(q, y_list[i])]

    s, y = s_list[-1], y_list[-1]
    gamma = _dot(s, y) / _dot(y, y)
    r = [gamma * x for x in q]

    for i in range(len(s_list)):
        beta = rho[i] * _dot(y_list[i], r)
        r = [x + s * (alpha[i] - beta) for x, s in zip(r, s_list[i])]

    return [-x for x in r]