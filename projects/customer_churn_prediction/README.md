# Customer Churn Prediction

## Problem

Customer churn is a critical problem for subscription-based businesses. Losing customers directly impacts revenue, and acquiring new customers is often more expensive than retaining existing ones.

This project aims to predict whether a customer is likely to churn based on their service usage, billing behavior, and account information.

---

## Objective

Build a classification model that identifies customers at risk of churning, with a focus on maximizing recall for the churn class to reduce missed churn cases.

---

## Dataset

The dataset contains customer-level information including:

* Demographics (Gender, Senior Citizen, Partner, Dependents)
* Account details (Tenure, Contract Type, Payment Method)
* Services (Internet Service, Streaming, Security features)
* Billing (Monthly Charges, Total Charges)

Target variable:

* `Churn Value`

  * 1 → Customer churned
  * 0 → Customer retained

---

## Data Preparation

### Key Steps

* Removed leakage features:

  * `Churn Label`, `Churn Score`, `Churn Reason`, `CLTV`
* Removed identifiers:

  * `CustomerID`, `Count`
* Dropped geographic features (low signal, high cardinality)
* Converted `Total Charges` to numeric
* Handled missing values (filled with 0 for new customers)

### Feature Engineering

* `Expected Charges = Tenure × Monthly Charges`
* `Charge Ratio = Total Charges / (Tenure + 1)`

---

## Modeling

Models evaluated:

* Logistic Regression
* Random Forest
* XGBoost

### Model Comparison

| Model               | Precision | Recall | F1   | ROC-AUC |
| ------------------- | --------- | ------ | ---- | ------- |
| Logistic Regression | 0.64      | 0.60   | 0.62 | 0.843   |
| Random Forest       | 0.64      | 0.52   | 0.57 | 0.826   |
| XGBoost             | 0.63      | 0.56   | 0.59 | 0.843   |

**Selected Model:** Logistic Regression
Reason: Higher recall with similar ROC-AUC compared to more complex models.

---

## Threshold Optimization

Default threshold (0.5) was not optimal due to class imbalance.

Using precision-recall analysis, threshold was adjusted:

* **Chosen Threshold: 0.3**

### Performance at Threshold = 0.3

| Class     | Precision | Recall | F1   |
| --------- | --------- | ------ | ---- |
| Non-Churn | 0.89      | 0.75   | 0.81 |
| Churn     | 0.52      | 0.75   | 0.61 |

### Impact

* Recall improved significantly (0.60 → 0.75)
* More churners correctly identified
* Acceptable drop in precision

---

## Error Analysis

Key failure patterns identified:

### 1. Medium-Tenure Customers

Customers with moderate tenure (not new, not long-term) are often misclassified.

→ Model struggles with ambiguous churn behavior.

---

### 2. High Charges but Loyal Customers

Customers with high monthly charges but long tenure are sometimes predicted as churn.

→ Model overweights billing features.

---

### 3. Boundary Uncertainty

Most misclassifications occur near the decision threshold.

→ Indicates overlapping feature space and inherent uncertainty.

---

## Key Insights

* Contract type and tenure are strong predictors of churn
* Monthly charges influence churn, but not independently
* Threshold selection significantly impacts business usefulness
* Model performance is limited by overlapping customer behavior patterns

---

## Limitations

* Moderate class overlap limits perfect classification
* No temporal behavior modeling (e.g., usage trends over time)
* Dataset lacks deeper behavioral signals

---

## Future Improvements

* Add interaction features (tenure × contract)
* Use calibrated probabilities
* Explore time-based features
* Segment-based modeling

---

## Conclusion

This project demonstrates that model performance is not just about choosing algorithms, but about:

* understanding errors
* aligning metrics with business goals
* making controlled, data-driven improvements

The final model prioritizes identifying churn risk over maximizing accuracy, making it more practical for real-world use.
