from bisect import bisect_right

def calibrate_isotonic(cal_labels, cal_probs, new_probs):
    """
    Apply isotonic regression calibration.
    """
    # Write code here
    data = sorted(zip(cal_probs, cal_labels))
    p = [x for x, _ in data]

    blocks = []
    for _, y in data:
        blocks.append([y, 1])
        while len(blocks) > 1 and blocks[-2][0] > blocks[-1][0]:
            s1, n1 = blocks.pop()
            s0, n0 = blocks.pop()
            blocks.append([(s0 * n0 + s1 * n1) / (n0 + n1), n0 + n1])

    c = []
    for v, n in blocks:
        c.extend([v] * n)

    res = []
    for q in new_probs:
        if q <= p[0]:
            res.append(c[0])
        elif q >= p[-1]:
            res.append(c[-1])
        else:
            i = bisect_right(p, q) - 1
            t = (q - p[i]) / (p[i + 1] - p[i])
            res.append(c[i] + t * (c[i + 1] - c[i]))

    return res