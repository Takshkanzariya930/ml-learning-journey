# Credit Default prediction Model

## 1. Context

### What problem does [this](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients) dataset address ? 
- This Dataset address problem that how many customers default their payment based on past bills and payments.
  
### Who would care about this prediction ?
-  Credit card providers want to identify the customers who will default before hand so that they can take appropriate actions to minimize risk.

## 2. Objective

### What exactly are you predicting ?
- we are predicting '1' or '0' and in this model or dataset or context '1' means YES they default next month and '0' means NO they will NOT default next month.

## 3. ML Framing 

### Type of problem
- This is **supervised binary classification** type problem. Because here we are predicting only one outcome out of two either customer will default or NOT next month.
- Also classes are **Imbalanced** because there are very less instances of default than of NOT default. and this may be case for many real life problems.

## 4. Success Criteria

### Why accuracy alone is insufficient ?
- As our data is imbalances accuracy may increase if model learns to answer every instance as NOT default. Because their are more instances of NOT default but it will fail to predict default cases completely.

### What metrics matter and why ?
- If not accuracy than which merit will successfully score our model and be accurate measure of it's performance. Answer is merits such as recall and ROC-AOC curve.
- Here cost of missing positive instant (false negative) is very high as it can directly lead to loss or default of customer so **recall** is mush better metric as for **ROC** and **AOC**. **ROC** is used to identify which threshold is better for model. and **AOC** is used to compare two different model at time of model selection. 