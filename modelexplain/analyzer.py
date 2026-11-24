from .metrics import calculate_accuracy, calculate_precision, calculate_recall


def analyze_model(actual, predicted):
    accuracy = calculate_accuracy(actual, predicted)
    precision = calculate_precision(actual, predicted)
    recall = calculate_recall(actual, predicted)

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "total_samples": len(actual)
    }