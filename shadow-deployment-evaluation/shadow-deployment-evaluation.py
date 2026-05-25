def evaluate_shadow(production_log, shadow_log, criteria):
    """
    Evaluate whether a shadow model is ready for promotion.
    """
    n = len(production_log)

    prod_correct = 0
    shadow_correct = 0
    agree = 0
    shadow_latencies = []

    for p, s in zip(production_log, shadow_log):
        prod_correct += (p["prediction"] == p["actual"])
        shadow_correct += (s["prediction"] == s["actual"])
        agree += (p["prediction"] == s["prediction"])
        shadow_latencies.append(s["latency_ms"])

    production_accuracy = prod_correct / n
    shadow_accuracy = shadow_correct / n
    accuracy_gain = shadow_accuracy - production_accuracy

    shadow_latencies.sort()
    idx = math.ceil(0.95 * n) - 1
    shadow_latency_p95 = shadow_latencies[idx]

    agreement_rate = agree / n

    promote = (
        accuracy_gain >= criteria["min_accuracy_gain"] and
        shadow_latency_p95 <= criteria["max_latency_p95"] and
        agreement_rate >= criteria["min_agreement_rate"]
    )

    return {
        "promote": promote,
        "metrics": {
            "shadow_accuracy": shadow_accuracy,
            "production_accuracy": production_accuracy,
            "accuracy_gain": accuracy_gain,
            "shadow_latency_p95": shadow_latency_p95,
            "agreement_rate": agreement_rate
        }
    }