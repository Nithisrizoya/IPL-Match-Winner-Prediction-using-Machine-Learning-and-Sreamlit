# IPL-Match-Winner-Prediction-using-Machine-Learning-and-Sreamlit

**Project Overview**
This project focuses on predicting the winner of an Indian Premier League (IPL) match using Machine Learning classification algorithms.

By leveraging historical IPL match data, the model learns patterns based on match conditions such as participating teams, toss winner, toss decision, and venue to predict the likely winning team.

This is a multi-class classification problem, as the target variable (winner) contains multiple team categories.

**Business Objective**

The goal of this project is to:

- Build a robust multi-class classification model

- Compare different ML algorithms

- Evaluate model performance using appropriate metrics

- Deploy the best-performing model using Streamlit

**Dataset Description**

- Dataset: IPL Historical Match Dataset

- Target Variable: winner

- Problem Type: Multi-class Classification

- Key Features Used:

1. team1

2. team2

3. toss_winner

4. toss_decision

5. venue

Other relevant categorical match attributes

**Data Preprocessing & Feature Engineering**

The following preprocessing steps were performed:

- Removed irrelevant columns:

id

date

player_of_match

Removed rows where winner = Unknown

- Handled categorical variables using:

pd.get_dummies() for feature encoding

LabelEncoder() for target encoding

- Ensured class balance using Stratified Train-Test Split

- Applied 5-Fold Cross Validation for reliable model evaluation

**Models Implemented & Compared**

The following machine learning algorithms were trained and evaluated:

- Logistic Regression

- K-Nearest Neighbors (KNN)

- Decision Tree Classifier

- Random Forest Classifier

XGBoost Classifier (Best Performing Model)

**Evaluation Metric Used:**

- F1 Macro Score (suitable for multi-class classification)

- 5-Fold Cross Validation

- XGBoost achieved the best overall performance and was selected as the final model.

**Final Model**

Algorithm: XGBoost Classifier

Handles multi-class classification effectively

Provides strong generalization performance

Evaluated using cross-validation for stability

The trained model was saved using pickle and integrated into a Streamlit web application.

**Streamlit Web Application**

- An interactive web application was developed using Streamlit to allow users to:

- Select match details via dropdown inputs

- Automatically encode input features

- Predict the match winner

- Display the predicted team in real time

**Technology Stack**

- Python

- Pandas

- NumPy

- Scikit-learn

- XGBoost

- Streamlit

- Pickle
