# Predicting Customer Experience Failures in E-commerce (with Implications for Fashion)
### Using Customer Experience Data to Identify and Manage Risk

## Executive Summary

Customer dissatisfaction in e-commerce is often treated as a reactive issue, but this analysis shows it is **predictable and concentrated in specific experience failures**.

Key findings:

* **Late delivery is the strongest driver of dissatisfaction**, with rates increasing sharply once orders fall behind expectations
* **Expectation gaps drive perception** — even “on-time” deliveries can generate dissatisfaction when expectations are not met
* **Customer feedback is incomplete**, meaning many negative experiences may go unobserved

A predictive model was developed to identify **high-risk orders before dissatisfaction is expressed**, enabling proactive intervention.

Business implications:

* Prioritize reducing late deliveries
* Implement **risk-based CX interventions**
* Monitor both explicit feedback and **silent customer segments**
* Align marketing promises with actual delivery performance

This project demonstrates how CX analytics can move from
**diagnosing problems → predicting risk → guiding action**,
enabling teams to intervene before negative experiences are formally expressed.

---

## Overview

This project demonstrates how customer dissatisfaction can be **predicted and proactively managed** by identifying where the post-purchase experience breaks down.

It combines:

* SQL-based data modeling
* Python-based analysis and feature engineering
* machine learning for risk prediction
* a prototype illustrating how insights translate into operational decisions

The underlying principle is simple:

> customer dissatisfaction emerges when delivered experience fails to meet expectations.

---

## Business Problem

Customer dissatisfaction is typically addressed after it occurs. This project instead focuses on identifying and managing it **before it escalates**.

It explores:

* What operational factors drive dissatisfaction
* How delivery performance shapes customer perception
* What can be learned from customers who do not leave feedback
* How to identify and act on high-risk orders

---

## Dataset

This project uses the **Olist Brazilian E-commerce Dataset** from Kaggle, including:

* Orders, customers, and reviews
* Item-level pricing and basket composition
* Delivery timestamps and estimated delivery dates
* Marketing funnel data (used as contextual input)

A key constraint:

> Not all customers leave reviews, meaning dissatisfaction is only partially observable.

---

## Project Structure

```plaintext
notebooks/
├── 00_sql_relations_and_queries.ipynb        # relational modeling
├── 01_data_cleaning_feature_engineering.ipynb
├── 02_eda.ipynb                             # core insights
├── 02b_marketing_analysis.ipynb              # expectation-setting layer
├── 03_modeling.ipynb                         # ML models & evaluation
├── 04_sfs-prototype_case-study.ipynb         # business application prototype

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
* Preserved missing reviews to reflect real-world feedback gaps

---

### 2. Feature Engineering

Key features:

* **delivery_delay**: actual vs estimated delivery
* **delivery_deviation_abs**: magnitude of expectation mismatch
* **order_value & product_count**: order complexity
* **avg_price_per_item**: pricing structure
* **prior_orders / is_repeat_customer**: customer history
* **time features**: month and weekday

Key variables:

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
* Feedback is biased toward extreme experiences

---

### 4. Marketing Context (Strategic Layer)

A separate analysis explores acquisition behavior:

* Different channels show different conversion patterns
* Suggests expectations are shaped before purchase
* Not directly linked to dissatisfaction (data limitation), but provides context

This extends the journey view:

> acquisition → expectation → experience → evaluation

---

### 5. Machine Learning Modeling

A predictive model was developed to identify orders at risk of dissatisfaction.

Models tested:

* Logistic Regression
* Random Forest
* Gradient Boosting (best performance)

Approach:

* Train/test split with stratification
* Hyperparameter tuning (RandomizedSearchCV)
* Evaluation using ROC-AUC, Recall, and F1-score

Key result:

> Delivery-related features are the strongest predictors of dissatisfaction.

---

### 6. Application Prototype (Operational CX Use Case)

The final notebook demonstrates how model predictions can be used operationally to manage customer experience risk.

In practice, these insights could inform fulfillment strategies such as Ship From Store (SFS), where faster or alternative fulfillment options help reduce delivery-related dissatisfaction.

It simulates:

* flagging high-risk orders
* prioritizing delayed shipments
* triggering proactive communication
* guiding service recovery actions

This positions the analysis as a decision-support tool, showing how dissatisfaction risk signals can be translated into concrete operational actions.

---

## Key Insights

1. **Delivery performance is the primary failure point**
   Late delivery is the strongest and most consistent driver of dissatisfaction

2. **Expectation gaps drive dissatisfaction**
   Customer perception is shaped by how reality compares to expectations

3. **Feedback is incomplete**
   Many negative experiences are not captured in review data

4. **Customer experience is end-to-end**
   Perception is shaped across the full journey:

   > acquisition → expectation → delivery → evaluation

---

## Business Recommendations

1. **Reduce late deliveries (highest impact)**
   Focus operational improvements where dissatisfaction risk is highest

2. **Implement risk-based interventions**
   Use model predictions to proactively manage at-risk orders

3. **Align expectations with operations**
   Ensure delivery promises reflect actual performance

4. **Monitor silent customers**
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
