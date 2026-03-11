def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    total_ref_count = sum(reference for reference in reference_counts)
    total_prod_count = sum(production for production in production_counts)

    TVD = 0
    for i in range(len(reference_counts)):
        pi = reference_counts[i] / total_ref_count
        qi = production_counts[i] / total_prod_count
        TVD += abs(pi - qi)

    TVD *= 0.5
    return {"score": TVD, "drift_detected": TVD > threshold}