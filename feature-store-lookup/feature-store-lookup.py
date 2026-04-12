def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    ans = []
    for request in requests:
        user_id = request["user_id"]
        user_features = request["online_features"]
        
        if user_id in feature_store:
            user_features = {**user_features, **feature_store[user_id]}
        else:
            user_features = {**user_features, **defaults}

        ans.append(user_features)

    return ans