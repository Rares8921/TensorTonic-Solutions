def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    # Write code here
    N, M = len(values), len(rewards[0])
    ans = [0] * N
    for s in range(N):
        max_q = -1000000000
        for a in range(M):
            q = rewards[s][a] + gamma * sum(transitions[s][a][s_next] * values[s_next] for s_next in range(N))
            max_q = max(max_q, q)

        ans[s] = max_q

    return ans