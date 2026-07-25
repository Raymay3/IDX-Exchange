# IDX Exchange - California Home Price Prediction

**Status:** 🚧 In Progress (Week 7 of 12)

Machine learning project completed as part of my **Data Science Internship at IDX Exchange**.

## Overview

The objective of this project is to develop a machine learning model capable of predicting the final sale price of residential properties in California using historical Multiple Listing Service (MLS) transaction data.

The exploratory analysis currently includes approximately **794,000 California property transactions**, with **399,000 residential single-family homes** retained after applying the project filtering criteria.

Throughout the internship, the project progresses from exploratory data analysis and preprocessing through feature engineering, model development, evaluation, and final presentation. The project includes engineered property features, school district information, and multiple machine learning models for predicting California home sale prices.

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
* Engineer meaningful predictive features
* Incorporate geographic information through school district mapping

---

## Model Progress

| Model             | Status     |         R² |
| ----------------- | ---------- | ---------: |
| Linear Regression | ✅ Complete | **0.7719** |
| Decision Tree     | ✅ Complete | **0.8045** |
| Random Forest     | ✅ Complete | **0.8696** |
| Gradient Boosting | ⏳ Planned  |          — |

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
│   ├── 01_exploration.ipynb      # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb
│   ├── 03_baseline_model.ipynb
│   ├── 04_model_comparison.ipynb
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
| 02_preprocessing.ipynb | Data cleaning, feature engineering, and preprocessing | ✅ Complete |
| 03_baseline_model.ipynb | Linear regression baseline model | ✅ Complete |
| 04_model_comparison.ipynb | Decision Tree, Random Forest, and model performance comparison | ✅ Complete |
| 05_advanced_models.ipynb | Try Gradient Boosting | ⏳ Planned |

---

## Technologies

* Python
* pandas
* GeoPandas
* NumPy
* scikit-learn
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
* XGBoost (planned)
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
* Engineered additional predictive property features.
* Added school district information using a spatial join with California school district boundaries.
* One-hot encoded selected categorical variables.
* Standardized continuous numerical features.
* Created a chronological train/test split using the most recent month as the testing set and a configurable training window preceding the test month (initially set to 5 months).
* Removed the top 0.5% of training sale prices after the chronological split to reduce the influence of extreme outliers while preserving an unbiased testing dataset.
* Exported cleaned training and testing datasets for model development.

## Preprocessing Highlights

Week 3 preprocessing included:

- Removed columns with 100% missing values.
- Removed variables containing more than 50% missing observations.
- Imputed remaining missing values using median (numerical) and mode (categorical) strategies.
- Removed identifier variables and project-designated data leakage features (`ListPrice` and `OriginalListPrice`).
- Engineered four additional predictive property features.
- Added school district information through a geographic spatial join.
- One-hot encoded selected low-cardinality categorical variables.
- Standardized continuous numerical predictor variables.
- Created a chronological training/testing split using the most recent month as the testing dataset and a configurable training window (initially five months) immediately preceding it.
- Removed the top 0.5% of training sale prices after the chronological split to reduce the impact of extreme outliers without modifying the testing dataset.

### Week 4

* Loaded the cleaned training and testing datasets produced during preprocessing.
* Trained a baseline Linear Regression model.
* Generated predictions on the testing dataset.
* Evaluated model performance using MAE, RMSE, R², MAPE, and MdAPE.
* Visualized actual versus predicted home sale prices.
* Established baseline performance for comparison with future machine learning models.

## Baseline Model Results

The baseline Linear Regression model establishes an initial benchmark for future model comparisons.

Performance on the testing dataset:

- R²: 0.7719
- MAE: $277,549
- RMSE: $471,470
- MAPE: 25.20%
- MdAPE: 18.64%

Although the baseline model captures a greater proportion of the variation in California home prices than earlier preprocessing iterations, there is still substantial room for improvement. More flexible machine learning algorithms are expected to better capture the nonlinear relationships present in residential real estate data.

These results serve as the baseline against which all future models in this project will be evaluated.

### Week 5

* Trained a Decision Tree Regression model.
* Trained a Random Forest Regression model.
* Evaluated all models using MAE, RMSE, R², MAPE, and MdAPE.
* Compared model performance against the Linear Regression baseline.
* Visualized Actual vs. Predicted home sale prices for each model.
* Examined Random Forest feature importance.
* Documented model strengths and limitations.
* Compared model performance after preprocessing improvements and training outlier filtering.

## Model Comparison Highlights

Week 5 model comparison found that:

- The Decision Tree model substantially improved prediction accuracy over the Linear Regression baseline.
- The Random Forest model achieved the strongest overall performance across all evaluation metrics.
- Prediction scatter plots showed the Random Forest produced predictions that most closely followed the ideal one-to-one relationship.
- Feature importance analysis identified bathrooms, geographic location, living area, and property age as the most influential predictors of California home sale prices.
- Random Forest achieved the highest R² (0.8696) while also producing the lowest MAE, RMSE, MAPE, and MdAPE among the models evaluated.

### Week 6

* Engineered four additional predictive property features.
* Added school district information through a spatial join using California school district boundaries.
* Retrained all machine learning models using the updated feature set.
* Compared model performance before and after feature engineering.
* Documented improvements in predictive accuracy across all models.

## Week 6 Highlights

Week 6 demonstrated that feature engineering substantially improved model performance.

- PropertyAge replaced YearBuilt as a more meaningful representation of home age.
- School district information provided more detailed geographic context than county alone.
- All three machine learning models improved after incorporating the engineered features.
- Linear Regression experienced the largest performance improvement.
- Random Forest remained the strongest overall model, achieving an R² of **0.8696**, MAE of **$183,336**, and RMSE of **$356,476**.

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

* Additional feature engineering
* Gradient Boosting regression models
* Hyperparameter tuning and model optimization
* Expanded model evaluation
* Streamlit prediction application (optional)
* Final project documentation and presentation

---

## License

This project is licensed under the MIT License.
