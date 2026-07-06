# IDX Exchange - California Home Price Prediction

**Status:** 🚧 In Progress (Week 4 of 12)

Machine learning project completed as part of my **Data Science Internship at IDX Exchange**.

## Overview

The objective of this project is to develop a machine learning model capable of predicting the final sale price of residential properties in California using historical Multiple Listing Service (MLS) transaction data.

The exploratory analysis currently includes approximately **794,000 California property transactions**, with **399,000 residential single-family homes** retained after applying the project filtering criteria.

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
├── data/
│   └── README.md                 # Dataset information (raw MLS files excluded)
├── notebooks/
│   └── 01_exploration.ipynb      # Exploratory Data Analysis
│   └── 02_preprocessing.ipynb
├── reports/
│   └── metadata_notes.md         # Dataset field descriptions
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Project Notebooks

| Notebook | Description | Status |
|----------|-------------|--------|
| 01_exploration.ipynb | Exploratory data analysis of California residential property sales | ✅ Complete |
| 02_preprocessing.ipynb | Data cleaning and preprocessing | ✅ Complete |
| 03_baseline_model.ipynb | Linear regression baseline model | ⏳ Planned |
| 04_tree_models.ipynb | Decision Tree and Random Forest models | ⏳ Planned |
| 05_feature_engineering.ipynb | Feature creation and selection | ⏳ Planned |

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

### Week 2

* Combined 30 monthly CRMLS Sold datasets into a single DataFrame
* Filtered data to Residential SingleFamilyResidence properties
* Performed exploratory data analysis (EDA)
* Evaluated missing values and summary statistics
* Visualized distributions of key housing variables
* Identified extreme observations and distribution skewness
* Documented findings for future preprocessing

## Exploratory Data Analysis Highlights

Week 2 exploratory analysis found that:

- The combined dataset contains approximately **794,000** property transactions.
- After filtering, **399,157** residential single-family properties remain.
- Missing values are minimal across the primary modeling variables.
- Close Price, Living Area, and Lot Size exhibit strongly right-skewed distributions.
- Most homes contain **3–4 bedrooms** and **2–3 bathrooms**.
- Extreme observations were identified and will be investigated during preprocessing.

### Week 3

* Removed columns containing 100% missing values.
* Removed variables with more than 50% missing data.
* Imputed remaining missing values using median and mode strategies.
* Removed identifier variables and data leakage features.
* One-hot encoded selected categorical variables.
* Standardized continuous numerical features.
* Created a chronological train/test split using the most recent month as the testing set and a configurable training window preceding the test month (initially set to 5 months).
* Exported cleaned training and testing datasets for model development.

## Preprocessing Highlights

Week 3 preprocessing included:

- Removed columns with 100% missing values.
- Removed variables containing more than 50% missing observations.
- Imputed remaining missing values using median (numerical) and mode (categorical) strategies.
- Removed identifier variables and project-designated data leakage features (`ListPrice` and `OriginalListPrice`).
- One-hot encoded selected low-cardinality categorical variables.
- Standardized continuous numerical predictor variables.
- Created a chronological training/testing split using the most recent month as the testing dataset and a configurable training window (initially five months) immediately preceding it.

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

* Baseline linear regression model
* Decision Tree and Random Forest models
* Feature engineering
* Gradient boosting models
* Model evaluation and comparison
* Feature importance analysis
* Prediction workflow
* Final project presentation

---

## License

This project is licensed under the MIT License.
