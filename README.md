# IDX Exchange - California Home Price Prediction

Machine learning project completed as part of my **Data Science Internship at IDX Exchange**.

## Overview

The objective of this project is to develop a machine learning model capable of predicting the final sale price of residential properties in California using historical Multiple Listing Service (MLS) transaction data.

Throughout the internship, the project will progress from exploratory data analysis and preprocessing through feature engineering, model development, evaluation, and final presentation.

This repository is updated throughout the internship to document my individual contributions and project progress.

---

## Objectives

* Explore historical California residential property data
* Clean and preprocess MLS datasets
* Engineer meaningful predictive features
* Train and compare multiple regression models
* Evaluate model performance using appropriate regression metrics
* Produce accurate property price predictions
* Document the complete machine learning workflow

---

## Project Timeline

| Week | Focus                                              |
| ---- | -------------------------------------------------- |
| 1    | Environment setup, dataset access, metadata review |
| 2    | Exploratory Data Analysis                          |
| 3    | Data preprocessing                                 |
| 4    | Baseline Linear Regression                         |
| 5    | Decision Tree & Random Forest                      |
| 6    | Feature Engineering                                |
| 7    | Gradient Boosting Models                           |
| 8    | Model Evaluation                                   |
| 9    | Streamlit Prediction App (Optional)                |
| 10   | Documentation                                      |
| 11   | Presentation Preparation                           |
| 12   | Final Presentation & Repository Handoff            |

---

## Repository Structure

```text
.
├── notebooks/
├── src/
├── reports/
├── models/
├── images/
├── data/
├── requirements.txt
└── README.md
```

---

## Technologies

* Python
* pandas
* NumPy
* scikit-learn
* matplotlib
* Jupyter Notebook

Additional libraries may be added as the project progresses.

---

## Current Progress

### Week 1

* Repository created
* Development environment configured
* Downloaded required CRMLS datasets
* Reviewed project documentation
* Reviewed property metadata
* Documented important dataset fields

---

## Dataset

The underlying California MLS property datasets are proprietary and are **not included** in this public repository.

This repository contains only my source code, notebooks, documentation, and supporting materials.

---

## Modeling Notes

The prediction target for this project is:

* **ClosePrice**

Following project guidance, the following variables will **not** be used as model features because they introduce target leakage:

* ListPrice
* OriginalListPrice

---

## Future Work

Future updates will include:

* Exploratory data analysis
* Data cleaning pipeline
* Feature engineering
* Regression model comparison
* Model evaluation
* Feature importance analysis
* Prediction workflow
* Final project presentation

---

## License

This project is licensed under the MIT License.
