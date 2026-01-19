# Credit Default prediction Model

## 1. Project Overview

### What problem is solves ?
- Many customer default their payment of their credit card which leads to huge losses to credit provider we are predicting as many customers which are at risk of default. So that credit provider can take appropriate action against it.

### Why it matters ?
- It matters because if we can predict "default" before it happens then we can prevent direct loss to credit provider.

## 2. Dataset

### Source
- This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license and is available [hear](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients).
- This dataset for the research aimed at the case of customer's default payments in Taiwan and compares the predictive accuracy of probability of default among six data mining methods. 

### Target variable
- Our target variable is "default payment next month" which binary values "0" means "Non-default" and "1" means "default".

### Class imbalance
- Their is class imbalance in our dataset which means from classes "default" (1) and "Non-default" (0). "Non-default" class is in majority while "default" is in minority. Their ratio is approx. 7:3.

## 3. Approach

### Cleaning
- We have done data cleaning in "analysis.ipynb" notebook in "Data Cleaning & Sanity Checks" section. In which we have checked for missing values (as their were no missing values we did not need to fill or remove any), We also checked for duplicates and dropped them from our dataset as they will decrease performance of model and We manually checked sanity of all the features.

### EDA
- We have done exploratory data analysis in "analysis.ipynb" notebook in "Exploratory Data Analysis (EDA)" section. In which we found how much data imbalance is their, How many outliers are their if any, which feature contributes most in prediction of our target and finally correlation matrix of whole dataset.

### Model tried
- We tried Logistic Regression as our baseline and Random Forest which we chose as our final model.

### Evaluation Strategy
- We used ROC-AUC as it is very reliable evaluation metric. Random Forest had high ROC-AUC than Logistic Regression although recall was low which is very important metric in our business case so we later fine tuned our model to increase it's performance.

## 4. Result

### Final Model
- Final model which is selected is Random Forest Classifier.

### Final Metrics

- test-set metrics - 
    - Accuracy :  0.6195561488403137
    - Precision :  0.3417385534173855
    - Recall :  0.7767722473604827
    - ROC-AUC :  0.7696328090333561

- Confusion Matrix : 
```python 
            [2683 1984]
            [ 296 1030]
```

### Chosen Threshold
- Chosen Threshold is 0.35. Reasoning is given in "Hyperparameter Tuning and Threshold Optimization" section of "analysis.ipynb" notebook.

## 5. Key Insight

### What mattered most
- Past months payment history definitely helped the most as also recall of the model helped the most as low recall lead to direct loss to credit provider.

### What didn’t help much
- Age alone did't helped much as it cannot contribute to prediction alone also accuracy of model did't helped because data was imbalanced.

## 6. Limitations

- Class imbalance still limits recall
- Model depends on historical behavior if modern behavior changes model must be updated.
- Since precision is low many "Non-default" customer would be flagged as "default" so requires manual checking. 

## 7. How to Run

### Dependencies
- "analysis.ipynb" is in notebooks folder of this directory.
- You can run this notebook in our local system if you have python, jupyter notebook, sklearn, numpy, pandas, seaborn and matplotlib.
- Or you can upload it on google colab to directly run this notebook without installing any dependencies. or click [hear](https://colab.research.google.com/github/Takshkanzariya930/ml-learning-journey/blob/master/04_projects/credit_default_prediction/notebooks/analysis.ipynb) to run notebook