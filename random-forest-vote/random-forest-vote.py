import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    N, M = len(predictions), len(predictions[0])
    ans = [0] * M

    from collections import defaultdict

    for j in range(M):
        fr = defaultdict(int)
        max_fr = -100000
        label = 0
        for i in range(N):
            fr[predictions[i][j]] += 1
            if fr[predictions[i][j]] > max_fr:
                max_fr = fr[predictions[i][j]]
                label = predictions[i][j]
            elif fr[predictions[i][j]] == max_fr:
                label = min(label, predictions[i][j])

        ans[j] = label
    
    return ans