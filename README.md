# Predict-Diabetes-with-Logistic-regression

Apply the logistic regression we learned in class to a new real-world dataset. The goal is to predict whether a patient has diabetes based on diagnostic measurements.

## Data Preparation
For this assignment, you will need to download the `diabetes.csv` dataset (commonly available on Kaggle or the UCI Machine Learning Repository) or load it directly using a URL in pandas.

The dataset contains the following medical predictor variables:
* Pregnancies
* Glucose
* BloodPressure
* SkinThickness
* Insulin
* BMI
* DiabetesPedigreeFunction
* Age

### Tasks
* **Task 1**: Write a Python script to load the data into a pandas DataFrame.
* **Task 2**: Separate the data into your features (X) and your target variable (y).
* **Task 3**: Split the dataset into a training set (75%) and a testing set (25%) using a random state of your choice.

## Model Building and Evaluation
Using scikit-learn, replicate the modeling process demonstrated in the lecture.

* **Task 4**: Initialize a Logistic Regression model. You may need to increase the `max_iter` parameter if you receive a convergence warning.
* **Task 5**: Train the model using your training data.
* **Task 6**: Use the trained model to make predictions on your testing data.
* **Task 7**: Generate and print both the Accuracy Score and the Confusion Matrix.

## Short Answer Reflection
After successfully running your code, answer the following questions based on your results. Add this response as a comment to your submission.

### Question 1
Look at your Confusion Matrix. How many **False Negatives** (patients who actually have diabetes, but the model predicted they do not) did your model produce?

### Question 2
In the context of the Breast Cancer dataset, a False Negative is extremely dangerous (telling a patient they are cancer-free when they actually have cancer). In the context of this Diabetes dataset, what are the real-world consequences of a False Negative versus a False Positive?
