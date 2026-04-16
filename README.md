# Predicting Customer Experience Failures in E-commerce
### From Operational Data to Proactive CX Risk Management (with Implications for Fashion)

## Executive Summary

Customer dissatisfaction in e-commerce is often addressed only after it occurs. This project demonstrates that dissatisfaction is predictable and systematically linked to operational failures, particularly delivery performance.

Key findings:

* **Late delivery is the strongest driver of dissatisfaction**, with rates increasing sharply once orders fall behind expectations
* **Expectation gaps drive perception** — even “on-time” deliveries can generate dissatisfaction when expectations are not met
* **Dissatisfaction remains defined through review behavior, which may still introduce bias**, even though this dataset provides high review coverage among delivered orders, allowing dissatisfaction to be directly observed.

A predictive model was developed to identify **high-risk orders before dissatisfaction is expressed**, enabling proactive intervention.

Business implications:

* Prioritize reducing late deliveries
* Implement **risk-based CX interventions**
* Use predictive signals to guide real-time decision-making
* Align delivery promises with operational performance

This project demonstrates how CX analytics can move from
**diagnosing problems → predicting risk → guiding action**,
enabling teams to intervene before negative experiences are formally expressed.

---

## Overview

This project demonstrates how customer dissatisfaction can be **predicted and proactively managed** by identifying where the post-purchase experience breaks down, using e-commerce customer experience data.

It combines:

* SQL-based data modeling
* Python-based analysis and feature engineering
* supervised machine learning for risk prediction
* unsupervised learning to identify experience profiles
* a prototype illustrating how insights can translate into real-world operational decisions

The underlying principle is simple:

> customer dissatisfaction emerges when delivered experience fails to meet expectations.

---

## Business Problem

Customer dissatisfaction is typically addressed after it occurs. This project instead focuses on identifying and managing it **before it escalates**.

It explores:

* What operational factors drive dissatisfaction
* How delivery performance shapes customer perception
* Predicting which orders are at risk before dissatisfaction occurs
* Translating insights into actionable CX strategies

---

## Dataset

This project uses the **Olist Brazilian E-commerce Dataset** from Kaggle, including:

* Orders, customers, and reviews
* Item-level pricing and basket composition
* Delivery timestamps and estimated delivery dates
* Marketing funnel data (used as contextual input)

Important note on data coverage:

> This dataset provides very high review coverage among delivered orders, allowing dissatisfaction to be directly observed rather than inferred from a small subset of feedback.

> However, dissatisfaction is still defined through review behavior, which may introduce bias in how experience is measured.

---

## Project Structure

```plaintext
notebooks/
├── 00_sql_relations_and_queries.ipynb        # relational modeling
├── 01_data_cleaning_feature_engineering.ipynb
├── 02_eda.ipynb                              # core insights
├── 02b_marketing_analysis.ipynb              # expectation-setting layer
├── 03_modeling.ipynb                         # ML models & evaluation
├── 04_sfs-prototype_case-study.ipynb         # business application prototype
├── utils.py                                  # graph aesthetics

data/
├── raw/
├── processed/

figures/
├── EDA visualizations

src/
├── main.py
```

---

## Methodology

### 1. SQL Data Modeling

* Built an order-level analytical dataset from relational tables
* Combined operational, customer, and review data
* Preserved order-level granularity for downstream analysis

---

### 2. Feature Engineering

Features were designed to capture key dimensions of customer experience:

* **Delivery performance**
delivery_delay, delivery_deviation_abs
* **Order complexity and value**
order_value, product_count, avg_price_per_item
* **Customer behavior**
prior_orders, is_repeat_customer
* **Time context**
purchase_month, purchase_dow

Target variables:

* `has_review` → whether feedback exists
* `is_dissatisfied` → dissatisfaction among reviewed orders

---

### 3. Exploratory Data Analysis

The analysis distinguishes between:

* **Observed dissatisfaction**
* **Silent customers (no review behavior)**

Key findings:

* Dissatisfaction rate ≈ **13% among reviewed orders**
* Late deliveries show a sharp increase in dissatisfaction (~75%)
* Even “on-time” deliveries show elevated dissatisfaction (~28%)
* Customer perception is driven by expectation gaps, not just absolute delay

---

### 4. Unsupervised Learning (Clustering)

KMeans clustering was applied to identify distinct customer experience profiles.

Key observations:

* A cluster of late deliveries with higher dissatisfaction risk
* A cluster of early, low-value orders with smoother experiences
* A cluster of on-time orders spanning higher values, representing commercially important transactions

This highlights that customer experience is not uniform and varies across operational patterns.

---

### 5. Marketing Context (Strategic Layer)

A separate analysis explores acquisition behavior:

* Different channels show varying conversion patterns
* Suggests that expectations are shaped before purchase
* Due to data limitations, this layer is contextual rather than directly linked to dissatisfaction.

This extends the journey view:

> acquisition → expectation → experience → evaluation

---

### 6. Machine Learning Modeling

A predictive model was developed to identify orders at risk of dissatisfaction.

Models tested:

* Logistic Regression
* Random Forest
* Gradient Boosting (best performance)

Approach:

* Train/test split with stratification
* Hyperparameter tuning (RandomizedSearchCV)
* Evaluation using ROC-AUC, Recall, and F1-score

Handling class imbalance:

* Dissatisfied orders are less frequent than satisfied ones.
* Therefore, Recall and F1-score were prioritized to better capture at-risk cases.

Key result:

> Delivery-related features are the strongest predictors of dissatisfaction.

---

### 7. Application Prototype (Operational CX Use Case)

The final notebook demonstrates how model predictions can be used operationally to manage customer experience risk.

In practice, these insights could inform fulfillment strategies such as Ship From Store (SFS), where faster or alternative fulfillment options help reduce delivery-related dissatisfaction.

It simulates:

* flagging high-risk orders
* prioritizing delayed shipments
* triggering proactive communication
* guiding service recovery actions

This illustrates how CX analytics can support real-time operational decision-making.

---

## Key Insights

1. **Delivery performance is the primary failure point**
   Late delivery is the strongest and most consistent driver of dissatisfaction

2. **Expectation gaps drive perception**
Customers react to differences between expected and actual delivery

3. **Customer experience is operationally driven**
Dissatisfaction is predictable from measurable features

4. **Customer experience is not uniform**
Different order types exhibit distinct experience patterns

---

## Business Recommendations

1. **Reduce late deliveries (highest impact)**
   Focus operational improvements where dissatisfaction risk is highest

2. **Implement risk-based interventions**
   Use model predictions to proactively manage at-risk orders

3. **Align expectations with operations**
   Ensure delivery promises reflect actual performance

4. **Ensure feedback data remains representative**
   Avoid relying solely on explicit feedback

5. **Integrate CX into operations**
   Use analytics to guide real-time decisions, as demonstrated in the prototype

---

## Limitations

* Dissatisfaction is only observed for customers who leave reviews
* Marketing and transaction data are not directly linked
* The model is primarily diagnostic (post-experience), not fully predictive pre-delivery

---

## Future Work

* Build a pre-delivery early-warning model
* Incorporate NLP analysis of review text
* Link acquisition channels to downstream outcomes
* Deploy a real-time CX monitoring system

---

## Author

Rachel Vianna,
Customer Experience & Data Analytics
