
# House Price Prediction — Regression Modeling

## Project Overview

This project explores regression modeling for predicting residential house prices using structured tabular data. The goal is to build a reproducible machine learning workflow covering data preprocessing, baseline modeling, and controlled experimentation with evaluation metrics.

The dataset contains housing attributes such as property size, quality ratings, construction year, neighborhood, and other structural features. The task is to estimate the **final sale price of each property**.

---

## Dataset

Source: Kaggle — *House Prices: Advanced Regression Techniques*

The dataset contains:

* ~1460 observations
* ~80 features
* Mixed feature types (numerical and categorical)

Target variable:

```
SalePrice
```

which represents the final selling price of the property.

---

## Problem Type

This is a **supervised regression problem** where the objective is to estimate a continuous numeric target.

---

## Evaluation Metrics

The primary evaluation metric used in this project is:

```
RMSE (Root Mean Squared Error)
```

RMSE measures the typical magnitude of prediction errors in the same units as the target variable (dollars), making it directly interpretable.

Additional metrics reported:

```
RMSLE
R² (coefficient of determination)
```

---

## Data Preprocessing

The preprocessing pipeline includes:

### Handling Missing Values

Highly sparse categorical features were removed due to limited signal:

```
PoolQC
MiscFeature
Alley
Fence
```

Categorical features representing structural absence were imputed with:

```
"None"
```

Examples:

```
GarageType
GarageFinish
GarageQual
BsmtQual
BsmtExposure
FireplaceQu
```

Numeric features with missing values were imputed using median or domain-appropriate defaults.

---

### Feature Encoding

Categorical variables were converted to numeric format using:

```
One-hot encoding
```

This allows linear models to learn category-specific coefficients.

---

## Baseline Model

A **Linear Regression model** was trained as the initial baseline.

Baseline performance:

```
RMSE   : 27,619
RMSLE  : 0.144
R²     : 0.900
```

Interpretation:

* The model explains approximately **90% of variance in housing prices**.
* The average prediction error is roughly **$27k**.

---

## Experiment: Log Transformation of Target

A log transformation of the target variable was evaluated to reduce right-skewness:

```
SalePrice → log1p(SalePrice)
```

Results:

| Model      | RMSE   | RMSLE | R²    |
| ---------- | ------ | ----- | ----- |
| Baseline   | 27,619 | 0.144 | 0.900 |
| Log Target | 23,126 | 0.131 | 0.930 |

Observation:

* Log transformation improved **RMSE**, **RMSLE** and **R$^2$**.
* Since RMSE is the primary evaluation metric, the log transformed target will be used to train model.

---

## Key Observations

* Structural features such as **overall quality, living area, and garage capacity** strongly influence price predictions.
* Linear regression performs reasonably well due to strong linear relationships in several engineered housing features.
* Target transformation improves proportional error but does not necessarily improve absolute prediction accuracy.

---

## Project Structure

```
house_price_regression
│
├── data
│   └── train.csv
|   └── data_description.txt 
│
├── dependencies
|   └── ml-env.yml
|
├── notebooks
│   └── analysis.ipynb
│
└── README.md
```

---

## Learning Focus

This project emphasizes:

* disciplined experimentation
* reproducible preprocessing
* clean data flow using pipleine
* model evaluation using interpretable metrics
* hypothesis-driven improvements

Rather than leaderboard optimization, the focus is on **developing reliable modeling workflows for tabular regression problems**.
