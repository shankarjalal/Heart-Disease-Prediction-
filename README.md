# **Heart Disease Prediction Using Machine Learning**

Summary

This project provides a detailed, end-to-end workflow for predicting heart disease risk using machine learning, with a strong emphasis on data-driven insights and visualizations.

Data Exploration & Visualization:  
The project begins with loading a heart disease dataset (918 records, 12 features). Exploratory Data Analysis (EDA) is performed using bar plots, histograms,
boxplots, violin plots, and correlation heatmaps. For example, the target variable `HeartDisease` shows a balanced distribution: approximately 54% positive cases and 46% negative cases.
Visualizations highlight key patterns, such as higher heart disease prevalence among certain chest pain types and age groups.

Data Cleaning & Preprocessing:  
Missing and anomalous values are addressed (e.g., zero cholesterol values, which are physiologically impossible, are replaced with the mean of valid entries).
Categorical variables are encoded using one-hot encoding, and numerical features are standardized. Duplicate records are checked and removed, ensuring data quality.

Feature Engineering:  
Relevant features are selected and engineered for optimal model performance. The final dataset includes both original and derived features, such as one-hot encoded categorical variables.

Model Building & Evaluation:  
The data is split into training (80%) and test (20%) sets. Six classification algorithms are evaluated: Logistic Regression, K-Nearest Neighbors (KNN),
Naive Bayes, Decision Tree, Random Forest, and Support Vector Machine (SVC).  
Model performance is assessed using accuracy and F1-score:

| Model                | Accuracy (%) | F1 Score (%) |
|----------------------|-------------|--------------|
| Logistic Regression  | 86.4        | 88.0         |
| **KNN**              | **86.9**    | **88.6**     |
| Naive Bayes          | 85.3        | 86.8         |
| Decision Tree        | 77.7        | 79.8         |
| Random Forest        | 86.4        | 88.2         |
| SVC                  | 84.8        | 86.8         |

KNN achieves the highest accuracy (86.9%) and F1-score (88.6%), making it the best-performing model.

Deployment:  
The trained KNN model, scaler, and feature columns are exported using joblib. A Streamlit web application is developed, enabling users to input their health
parameters and receive real-time heart disease risk predictions.

Conclusion:  
This workflow demonstrates a robust, reproducible approach to clinical machine learning for heart disease risk assessment. The combination of thorough EDA, 
rigorous preprocessing, comparative model evaluation, and interactive deployment ensures both transparency and practical utility. The project is well-documented and 
suitable for further research or real-world application.
