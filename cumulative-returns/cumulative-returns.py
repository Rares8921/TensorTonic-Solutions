def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    ans = []
    wt = 1
    for r in returns:
        wt *= (1 + r)
        ans.append(wt - 1)

    return ans