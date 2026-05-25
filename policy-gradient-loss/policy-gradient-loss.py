import numpy as np

def policy_gradient_loss(log_probs, rewards, gamma):
    """
    Compute REINFORCE policy gradient loss with mean-return baseline.
    """
    log_probs = np.asarray(log_probs, dtype=float)
    rewards = np.asarray(rewards, dtype=float)
    n = len(rewards)

    returns = np.zeros(n)
    g = 0.0

    for t in range(n - 1, -1, -1):
        g = rewards[t] + gamma * g
        returns[t] = g

    baseline = returns.mean()
    advantages = returns - baseline

    loss = -np.mean(log_probs * advantages)
    return float(loss)