def sarsa_update(q_table, state, action, reward, next_state, next_action, alpha, gamma):
    """
    Perform one SARSA update and return the updated Q-table.
    """
    delta = reward + gamma * q_table[next_state][next_action] - q_table[state][action]
    Q_new = q_table.copy()
    Q_new[state][action] = Q_new[state][action] + alpha * delta

    return Q_new