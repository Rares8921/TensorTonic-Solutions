from datetime import datetime as dt

def promote_model(models):
    best_model = None
    highest_accuracy = -1
    lowest_latency = float('inf')
    latest_timestamp = None

    for model in models:
        name = model["name"]
        accuracy = model["accuracy"]
        latency = model["latency"]
        timestamp = dt.strptime(model["timestamp"], "%Y-%m-%d")

        if (
            best_model is None
            or accuracy > highest_accuracy
            or (
                accuracy == highest_accuracy and (
                    latency < lowest_latency or
                    (latency == lowest_latency and timestamp > latest_timestamp)
                )
            )
        ):
            best_model = name
            highest_accuracy = accuracy
            lowest_latency = latency
            latest_timestamp = timestamp

    return best_model