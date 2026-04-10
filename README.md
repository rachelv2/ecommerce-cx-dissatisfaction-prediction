# E-commerce Customer Experience & Dissatisfaction Prediction

## Executive Summary

Customer dissatisfaction in e-commerce is often treated as a reactive issue, but this analysis shows it is **predictable and concentrated in specific experience failures**.

Key findings:

* **Late delivery is the strongest driver of dissatisfaction**, with rates increasing dramatically once orders fall behind expectations
* **Expectation gaps matter more than absolute timing** — even “on-time” deliveries can generate dissatisfaction when expectations are not met
* **Customer feedback is incomplete**, meaning many negative experiences may go unobserved

Using these insights, a machine learning model was built to identify **high-risk orders before dissatisfaction is expressed**, enabling proactive intervention.

Business implications:

* Focus operational efforts on reducing late deliveries
* Implement **risk-based customer experience interventions**
* Monitor not only explicit feedback, but also **silent customer segments**
* Align marketing promises with actual delivery performance

This project demonstrates how customer experience analytics can move from **diagnosing problems → predicting risk → guiding action**.

In a real-world setting, this approach could reduce dissatisfaction by enabling teams to intervene before negative experiences are formalized through customer feedback.

---

## Overview

This project shows how customer dissatisfaction in e-commerce can be predicted and proactively managed by identifying where the post-purchase experience breaks down. 

It builds machine learning models to predict at-risk orders, and demonstrates how those predictions can be used in a real business context.

The core idea is that **customer dissatisfaction is not random** — it emerges when the experience delivered falls short of the expectations set before purchase.

This project combines:

* SQL-based data modeling
* Python-based feature engineering and analysis
* machine learning for prediction
* and a prototype showing how insights can drive operational decisions

---

## Business Problem

In e-commerce, customer dissatisfaction is often treated as a reactive issue.

This project reframes it as a **predictable outcome of experience gaps**, asking:

* What operational factors drive dissatisfaction?
* How does delivery performance influence perception?
* Are there “silent” customers whose experience is not captured in reviews?
* Can we predict which orders are at risk and intervene proactively?

---

## Dataset

This project uses the **Olist Brazilian E-commerce Dataset** from Kaggle, including:

* Orders, customers, and reviews
* Item-level pricing and basket composition
* Delivery timestamps and estimated delivery dates
* Marketing funnel data (used as a contextual layer)

A key nuance:

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
* Joined orders, customers, reviews, and item-level data
* Preserved missing reviews to reflect real-world feedback gaps

---

### 2. Feature Engineering

Key features include:

* **delivery_delay**: difference between actual and estimated delivery
* **delivery_deviation_abs**: magnitude of expectation mismatch
* **order_value & product_count**: order complexity
* **avg_price_per_item**: price structure
* **prior_orders / is_repeat_customer**: customer history
* **time features**: month and weekday

Two key variables:

* `has_review` → whether feedback exists
* `is_dissatisfied` → dissatisfaction among reviewed orders

---

### 3. Exploratory Data Analysis

The analysis focuses on both:

* **Observed dissatisfaction**
* **Silent customers (no review behavior)**

Key findings:

* Dissatisfaction rate ≈ **13% among reviewed orders**
* Late deliveries dramatically increase dissatisfaction (~75%)
* Even “on-time” deliveries show elevated dissatisfaction (~28%)
* Customers who leave reviews differ from those who remain silent
* Extreme experiences drive written feedback

---

### 4. Marketing Context (Strategic Layer)

A separate analysis explores acquisition channels:

* Channels differ in conversion behavior
* Suggests expectations are shaped before purchase
* Not causally linked to dissatisfaction (data limitation), but provides context

This extends the customer journey view:

> acquisition → expectation → experience → evaluation

---

### 5. Machine Learning Modeling

A predictive model was developed to identify orders at risk of customer dissatisfaction.

#### Models built:

* Logistic Regression (baseline, interpretable)
* Random Forest (captures non-linear patterns)
* Gradient Boosting (best performance)

#### Techniques:

* Train/test split with stratification
* Hyperparameter tuning (RandomizedSearchCV)
* Evaluation using:

  * ROC-AUC
  * Recall (dissatisfied class)
  * F1-score

#### Outcome:

* Gradient Boosting selected as best model
* Delivery-related features are the strongest predictors

---

### 6. Application Prototype (SFS Case Study)

The final notebook demonstrates how the model could be used in a real business setting.

It shows how predicted dissatisfaction risk can be operationalized to support decision-making.

This includes:

* flagging high-risk orders
* prioritizing delayed shipments
* triggering proactive communication
* guiding service recovery actions

This shifts the project from:

> **prediction → action**

and frames it as a **decision-support tool for customer experience teams**.

---

## Key Insights

### 1. Delivery performance is the dominant driver

Late delivery sharply increases dissatisfaction.

### 2. Expectation gaps matter

Customer dissatisfaction is driven by expectation gaps, not just operational failures.

### 3. Customer feedback is incomplete

Many customers do not leave reviews, meaning:

> observed dissatisfaction ≠ total dissatisfaction

### 4. Experience is end-to-end

Customer perception is shaped across the full journey:

> acquisition → expectation → delivery → evaluation

---

## Business Recommendations

### 1. Reduce late deliveries (highest impact)

Late delivery is the primary operational driver of dissatisfaction.

### 2. Implement risk-based intervention

Use model predictions to:

* flag high-risk orders
* prioritize proactive communication
* trigger service recovery workflows

### 3. Focus on expectation management

Align delivery promises with actual operational performance to reduce expectation-driven dissatisfaction.

### 4. Monitor silent customers

Do not rely only on review data to assess customer experience.

### 5. Integrate CX into operations

Use analytics to guide real-time decision-making, as demonstrated in the prototype.

---

## Limitations

* Dissatisfaction is only observed for customers who leave reviews
* Marketing and transaction data are not directly linked
* The model is primarily diagnostic (post-experience), not fully predictive pre-delivery

---

## Future Work

* Build an early-warning model using only pre-delivery features
* Incorporate NLP analysis of review text
* Link acquisition channels to downstream experience
* Deploy a real-time CX monitoring system

---

## Author

Rachel Vianna
Customer Experience & Data Analytics
