def retraining_policy(daily_stats, config):
    """
    Decide which days to trigger model retraining.
    """
    drift_threshold = config["drift_threshold"]
    performance_threshold = config["performance_threshold"]
    max_staleness = config["max_staleness"]
    cooldown = config["cooldown"]
    retrain_cost = config["retrain_cost"]
    budget = config["budget"]

    retrains = []
    days_since_retrain = 0
    last_retrain_day = None

    for stat in daily_stats:
        day = stat["day"]

        days_since_retrain += 1

        trigger = (
            stat["drift_score"] > drift_threshold or
            stat["performance"] < performance_threshold or
            days_since_retrain >= max_staleness
        )

        cooldown_ok = (
            last_retrain_day is None or
            day - last_retrain_day >= cooldown
        )

        budget_ok = budget >= retrain_cost

        if trigger and cooldown_ok and budget_ok:
            retrains.append(day)
            budget -= retrain_cost
            days_since_retrain = 0
            last_retrain_day = day

    return retrains