ModelExplain – Python Model Evaluation Library

1. Project Description

ModelExplain is a Python-based library developed to evaluate and analyze the performance of machine learning classification models. It provides simple functions to calculate important evaluation metrics such as Accuracy, Precision, and Recall.

The main purpose of this project is to make model evaluation easier by providing reusable Python functions. Instead of writing the same evaluation calculations repeatedly, users can import the functions from the ModelExplain library and use them in their Python programs.

This project is developed using pure Python and does not require heavy external machine learning libraries for its basic calculations.

2. Objectives of the Project

The main objectives of ModelExplain are:

To develop a simple and reusable Python library for model evaluation.

To calculate the accuracy of classification predictions.

To calculate precision and recall values.

To provide a combined model analysis function.

To improve code reusability and maintainability.

To test the implemented functions using automated testing.

3. Features

3.1 Accuracy Calculation

Accuracy measures the overall percentage of correct predictions made by a model.

3.2 Precision Calculation

Precision measures how many of the positive predictions made by the model are actually positive.

3.3 Recall Calculation

Recall measures how many of the actual positive cases are correctly identified by the model.

3.4 Model Analysis

The library provides an analyze_model() function that calculates Accuracy, Precision, Recall, and Total Samples together.

3.5 Automated Testing

Pytest is used to verify the correctness of the implemented functions through automated test cases.

4. Technologies Used

Programming Language: Python

Testing Framework: Pytest

Code Editor: Visual Studio Code

Development Environment: Python Virtual Environment (venv)

5. Project Structure

ModelExplain/
│
├── examples/
│   └── example.py
│
├── modelexplain/
│   ├── __init__.py
│   ├── analyzer.py
│   └── metrics.py
│
├── tests/
│   └── test_metrics.py
│
├── main.py
├── README.md
├── requirements.txt
└── venv/

Description of Files

metrics.py: Contains functions to calculate Accuracy, Precision, and Recall.

analyzer.py: Combines the evaluation metrics and provides a complete model analysis result.

init.py: Makes the modelexplain directory recognizable as a Python package.

example.py: Demonstrates how to use the ModelExplain library.

test_metrics.py: Contains automated test cases for checking metric calculations.

main.py: Provides the main program to execute and display model evaluation results.

requirements.txt: Lists the required Python packages.

README.md: Contains project documentation and usage instructions.

6. How It Works

ModelExplain takes two input lists:

Actual values – The correct or expected output labels.

Predicted values – The output labels predicted by the model.

The library compares these two lists and calculates the evaluation metrics.

Evaluation Formulas

Accuracy

Accuracy is calculated by dividing the number of correct predictions by the total number of predictions.

Formula:

Accuracy = Correct Predictions / Total Predictions

Precision

Precision is calculated by dividing True Positives by the total number of positive predictions.

Formula:

Precision = TP / (TP + FP)

Recall

Recall is calculated by dividing True Positives by the total number of actual positive cases.

Formula:

Recall = TP / (TP + FN)

Where:

TP = True Positive

FP = False Positive

FN = False Negative

7. Installation and Setup

Follow these steps to run the project:

Step 1: Install Python on your computer.

Step 2: Open the ModelExplain project folder in Visual Studio Code.

Step 3: Open the terminal and activate the virtual environment.

Step 4: Install the required package using:

pip install -r requirements.txt

Step 5: Run the main program:

python main.py

8. Usage Example

The following example demonstrates how to use the ModelExplain library.

from modelexplain.analyzer import analyze_model

actual = [1, 0, 1, 1, 0]
predicted = [1, 0, 0, 1, 0]

result = analyze_model(actual, predicted)

print("Model Analysis Results")
print("Accuracy:", result["accuracy"])
print("Precision:", result["precision"])
print("Recall:", result["recall"])
print("Total Samples:", result["total_samples"])

9. Sample Output

When the main program is executed, the following output is displayed:

Welcome to ModelExplain
-----------------------
Accuracy: 0.8
Precision: 1.0
Recall: 0.6666666666666666
Total Samples: 5

The output shows that the model correctly predicted 80% of the total samples. The precision value is 1.0, indicating that all positive predictions were correct. The recall value is approximately 0.667, indicating that the model identified two-thirds of the actual positive cases.

10. Testing

Testing is an important part of the development process. The ModelExplain library uses Pytest to verify the correctness of its functions.

The project includes seven test cases:

Test for perfect accuracy.

Test for partial accuracy.

Test for zero accuracy.

Test for empty input lists.

Test for different input list lengths.

Test for precision calculation.

Test for recall calculation.

To execute all test cases, use:

python -m pytest

All seven test cases passed successfully during testing.

11. Limitations

The current implementation is designed for binary classification using labels 0 and 1.

It accepts actual and predicted values as Python lists.

It focuses on basic evaluation metrics rather than advanced model interpretation.

It does not directly train machine learning models.

It does not currently provide graphical visualizations of evaluation results.

12. Future Enhancements

The project can be improved in the future by adding:

Support for multiclass classification.

Additional evaluation metrics such as F1-score.

Confusion matrix generation.

Graphical visualization of model performance.

Improved input validation and error handling.

More automated test cases.

13. Conclusion

ModelExplain is a simple and reusable Python library developed to evaluate classification model performance. It provides essential evaluation metrics such as Accuracy, Precision, and Recall through easy-to-use functions.

The project demonstrates the practical use of Python functions, modular programming, package organization, and automated testing using Pytest.

Through this project, a basic understanding of model evaluation and Python library development can be achieved. The library can also be extended with additional evaluation features in future versions.