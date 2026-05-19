from math import ceil

def winsorize(values, lower_pct, upper_pct):
    """
    Clip values at the given percentile bounds.
    """
    tmp = values.copy()
    srtd = sorted(tmp)
    n = len(tmp)
    k_min = (n - 1) * lower_pct / 100
    mini = srtd[int(k_min)] + (k_min - int(k_min)) * (srtd[ceil(k_min)] - srtd[int(k_min)])

    k_max = (n - 1) * upper_pct / 100
    maxi = srtd[int(k_max)] + (k_max - int(k_max)) * (srtd[ceil(k_max)] - srtd[int(k_max)])

    for i in range(n):
        if values[i] < mini:
            values[i] = mini

        if values[i] > maxi:
            values[i] = maxi

    return values

    