def edit_distance(s1, s2):
    """
    Compute the minimum edit distance between two strings.
    """
    if len(s1) == 0 and len(s2) == 0:
        return 0
    elif len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)
    
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n + 2)] for _ in range(m + 2)]

    # init
    for i in range(m):
        dp[i][0] = i
    for j in range(n):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]