from modelexplain.analyzer import analyze_model

actual = [1, 0, 1, 1, 0]
predicted = [1, 0, 0, 1, 0]

result = analyze_model(actual, predicted)

print("Welcome to ModelExplain")
print("-----------------------")
print("Accuracy:", result["accuracy"])
print("Precision:", result["precision"])
print("Recall:", result["recall"])
print("Total Samples:", result["total_samples"])
