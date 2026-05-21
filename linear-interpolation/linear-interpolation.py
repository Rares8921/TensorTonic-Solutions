def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    n = len(values)
    left, right = [0] * n, [0] * n
    for i, x in enumerate(values):
        if i == 0:
            continue
            
        left[i] = left[i - 1] if x is None else i

    for i, x in reversed(list(enumerate(values))):
        if i == n - 1:
            right[i] = n - 1
            continue
            
        right[i] = right[i + 1] if x is None else i

    ans = []
    for i, x in enumerate(values):
        if x is None:
            l, r = left[i], right[i]
            v_left, v_right = values[l], values[r]
            new_value = v_left + (i - l) / (r - l) * (v_right - v_left)
            ans.append(new_value)
        else:
            ans.append(x)

    return ans