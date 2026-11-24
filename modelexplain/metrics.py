def calculate_accuracy(actual, predicted):
    if len(actual) != len(predicted):
        raise ValueError("Both lists must have the same length")

    if len(actual) == 0:
        return 0.0

    correct = sum(a == p for a, p in zip(actual, predicted))
    return correct / len(actual)
def calculate_precision(actual, predicted):
    true_positive = sum(a == 1 and p == 1 for a, p in zip(actual, predicted))
    false_positive = sum(a == 0 and p == 1 for a, p in zip(actual, predicted))

    if true_positive + false_positive == 0:
        return 0.0

    return true_positive / (true_positive + false_positive)


def calculate_recall(actual, predicted):
    true_positive = sum(a == 1 and p == 1 for a, p in zip(actual, predicted))
    false_negative = sum(a == 1 and p == 0 for a, p in zip(actual, predicted))

    if true_positive + false_negative == 0:
        return 0.0

    return true_positive / (true_positive + false_negative)