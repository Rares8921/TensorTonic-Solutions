from collections import Counter

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    n = len(X_test)
    maj = Counter(y_train).most_common(1)[0][0]

    return [maj] * n