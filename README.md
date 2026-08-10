# IDX Exchange - California Home Price Prediction

**Status:** 🚧 In Progress (Week 9 of 12)

**Last Updated:** August 2026

Machine learning project completed as part of my **Data Science Internship at IDX Exchange**.

## Overview

The objective of this project is to develop a machine learning model capable of predicting the final sale price of residential properties in California using historical Multiple Listing Service (MLS) transaction data.

The project uses monthly California CRMLS Sold transaction data. Initial exploratory analysis combined approximately **794,000 property transactions**, with approximately **399,000 residential single-family homes** retained during the initial filtering stage.

As the preprocessing pipeline was expanded with additional monthly data and refined filtering rules, the modeling dataset grew to **411,984 valid California residential single-family property sales** before the final chronological train/validation/test split.

Throughout the internship, the project progresses from exploratory data analysis and preprocessing through feature engineering, model development, evaluation, and final presentation. The project includes engineered property features, geographic school district information obtained through a spatial join, and multiple machine learning models ranging from Linear Regression to XGBoost for predicting California home sale prices.

This repository is updated throughout the internship to document my individual contributions and project progress.

---

## Objectives

* Explore historical California residential property data
* Clean and preprocess MLS datasets
* Engineer meaningful predictive features
* Incorporate detailed geographic information through school district mapping
* Train and compare multiple regression models
* Perform validation-based hyperparameter tuning
* Evaluate model performance using multiple regression metrics and price segments
* Produce accurate property price predictions
* Document the complete machine learning workflow

---

## Model Progress

| Model | Status | R² |
|---|---|---:|
| Linear Regression | ✅ Complete | **0.7381** |
| Decision Tree | ✅ Complete | **0.7949** |
| Random Forest | ✅ Complete | **0.8815** |
| XGBoost | ✅ Complete | **0.9024** |

---

## Current Best Model

The strongest model developed so far is the final tuned **XGBoost** model.

The selected configuration uses:

- **300 estimators**
- **Maximum tree depth of 8**
- **Learning rate of 0.1**

Performance on the final testing dataset:

- **R²:** 0.9024
- **MAE:** $160,177.50
- **RMSE:** $307,515.58
- **MAPE:** 12.23%
- **MdAPE:** 8.46%

This configuration was selected using a dedicated validation period and then retrained using the combined training and validation data before final evaluation on the untouched testing period.

XGBoost currently provides the strongest predictive performance among all models evaluated in the project.

---

## Final Model Comparison

| Model | R² | MAE | RMSE | MAPE | MdAPE |
|---|---:|---:|---:|---:|---:|
| Linear Regression | 0.7381 | $303,048 | $503,602 | 27.47% | 20.57% |
| Decision Tree | 0.7949 | $222,391 | $445,657 | 16.41% | 10.59% |
| Random Forest | 0.8815 | $173,400 | $338,823 | 13.14% | 8.98% |
| **XGBoost** | **0.9024** | **$160,178** | **$307,516** | **12.23%** | **8.46%** |

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
│   └── README.md                  # Dataset information (raw MLS files excluded)
├── notebooks/
│   ├── 01_exploration.ipynb       # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb     # Data cleaning and feature engineering
│   ├── 03_baseline_model.ipynb    # Linear Regression baseline
│   ├── 04_model_comparison.ipynb  # Decision Tree and Random Forest
│   ├── 05_advanced_models.ipynb   # XGBoost and hyperparameter tuning
│   └── 06_evaluation.ipynb        # Expanded model evaluation
├── reports/
│   ├── metadata_notes.md          # Dataset field descriptions
│   └── metrics_summary.csv        # Final model performance metrics
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Project Notebooks

| Notebook | Description | Status |
|---|---|---|
| 01_exploration.ipynb | Exploratory analysis of California residential property sales | ✅ Complete |
| 02_preprocessing.ipynb | Data cleaning, feature engineering, geographic enrichment, encoding, and preprocessing | ✅ Complete |
| 03_baseline_model.ipynb | Linear Regression baseline model | ✅ Complete |
| 04_model_comparison.ipynb | Decision Tree, Random Forest, feature comparison, and model evaluation | ✅ Complete |
| 05_advanced_models.ipynb | XGBoost development and validation-based hyperparameter tuning | ✅ Complete |
| 06_evaluation.ipynb | Expanded evaluation using MAPE, MdAPE, and home price bands | ✅ Complete |

---

## Technologies

* Python
* Visual Studio Code
* pandas
* GeoPandas
* NumPy
* scikit-learn
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
* XGBoost
* matplotlib

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

* Combined monthly CRMLS Sold datasets and filtered to residential single-family properties.
* Removed properties located outside California.
* Removed columns containing 100% missing values and variables exceeding the missing-data threshold.
* Removed identifier variables and known data leakage features.
* Removed invalid sale-price observations.
* Engineered additional predictive property features.
* Added school district information using a spatial join with California School District Areas (2024–2025).
* Resolved overlapping school district boundaries by retaining Unified districts where available and High School districts otherwise.
* Created a chronological training, validation, and testing framework.
* Used May 2026 as the validation period and June 2026 as the final testing period.
* Applied sale-price outlier filtering independently to the training, validation, and testing periods using cutoffs learned from the training data.
* Learned missing-value imputation values from the training data only.
* Target encoded school district information using 5-fold out-of-fold encoding for the training set.
* One-hot encoded remaining low-cardinality categorical variables.
* Standardized continuous numerical features using parameters learned from the training data only.
* Exported cleaned training, validation, and testing datasets for model development.

## Preprocessing Highlights

The final preprocessing pipeline includes:

- California-only residential single-family property filtering.
- Removal of identifiers and project-designated leakage features (`ListPrice` and `OriginalListPrice`).
- Four engineered property features:
  - `PropertyAge`
  - `BathroomBedroomRatio`
  - `LivingAreaPerBedroom`
  - `LotSizePerLivingArea`
- Detailed geographic information from California school district boundaries.
- Leakage-safe school district target encoding using 5-fold out-of-fold encoding.
- One-hot encoding for remaining low-cardinality categorical variables.
- Training-derived missing-value imputation and feature scaling.
- A chronological **training / validation / testing** design.
- **103 final predictor features**.

### Week 4

* Loaded the cleaned training, validation, and testing datasets produced during preprocessing.
* Trained a baseline Linear Regression model.
* Generated predictions on the testing dataset.
* Evaluated model performance using MAE, RMSE, R², MAPE, and MdAPE.
* Visualized actual versus predicted home sale prices.
* Established baseline performance for comparison with future machine learning models.

## Baseline Model Results

The final Linear Regression baseline establishes the benchmark for comparison with more flexible machine learning models.

Performance on the final testing dataset:

- **R²:** 0.7381
- **MAE:** $303,048.15
- **RMSE:** $503,601.63
- **MAPE:** 27.47%
- **MdAPE:** 20.57%

The baseline captures a substantial portion of the variation in California home sale prices but produces considerably larger dollar- and percentage-based errors than the tree-based and gradient boosting models developed later in the project.

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

- Decision Tree substantially improved prediction accuracy over the Linear Regression baseline.
- Random Forest substantially improved performance beyond both Linear Regression and the individual Decision Tree.
- Final Decision Tree testing performance reached an **R² of 0.7949**, **MAE of $222,391**, and **RMSE of $445,657**.
- Final Random Forest testing performance reached an **R² of 0.8815**, **MAE of $173,400**, and **RMSE of $338,823**.
- Random Forest also achieved a **MAPE of 13.14%** and **MdAPE of 8.98%**.
- Feature importance identified the target-encoded school district feature (`DistrictName_TE`) and `LivingArea` as the two most influential predictors in the final Random Forest model.
- Geographic coordinates and engineered property characteristics also contributed to the model's predictions.

### Week 6

* Engineered four additional predictive property features.
* Added detailed school district information through a spatial join with California school district boundaries.
* Replaced high-dimensional school district one-hot encoding with target encoding in the current preprocessing pipeline.
* Reduced the final feature space to 103 predictor variables.
* Retrained Linear Regression, Decision Tree, and Random Forest using the updated feature-engineered dataset.
* Compared original and updated feature sets and model performance.

## Week 6 Highlights

Week 6 demonstrated the value of adding engineered property characteristics and more detailed geographic information.

- `PropertyAge` provides a direct representation of home age at the time of sale.
- Ratio features capture relationships among bedrooms, bathrooms, living area, and lot size.
- School district information provides more detailed geographic context than county-level location alone.
- Target encoding allows detailed school district information to be retained without creating hundreds of district dummy variables.
- The current Random Forest model achieves an **R² of 0.8815**, **MAE of $173,400**, **RMSE of $338,823**, **MAPE of 13.14%**, and **MdAPE of 8.98%**.
- `DistrictName_TE` is the most important feature in the final Random Forest model.

### Week 7

* Trained four XGBoost regression configurations.
* Performed light hyperparameter tuning of `n_estimators`, `max_depth`, and `learning_rate`.
* Evaluated candidate configurations using the dedicated validation dataset.
* Selected the strongest configuration without using the final testing period for model-selection decisions.
* Retrained the selected configuration using the combined training and validation datasets.
* Evaluated the final XGBoost model on the untouched testing period.
* Compared XGBoost against Linear Regression, Decision Tree, and Random Forest.

## Week 7 Highlights

Week 7 demonstrated that gradient boosting further improved predictive performance.

- Four XGBoost configurations were evaluated using validation-based hyperparameter tuning.
- Increasing `n_estimators` from 100 to 200 improved validation performance.
- Increasing `max_depth` from 6 to 8 produced an additional improvement.
- Reducing `learning_rate` from 0.3 to 0.1 while increasing `n_estimators` to 300 produced the strongest validation results.
- The selected configuration uses **300 estimators**, **maximum depth 8**, and **learning rate 0.1**.
- After retraining on the combined training and validation data, the final XGBoost model achieved an **R² of 0.9024**, **MAE of $160,177.50**, **RMSE of $307,515.58**, **MAPE of 12.23%**, and **MdAPE of 8.46%**.
- XGBoost achieved the strongest final testing performance across all five evaluation metrics.

### Week 8

* Expanded model evaluation beyond R² using MAE, RMSE, MAPE, and MdAPE.
* Consolidated final performance metrics for all four models.
* Exported the model comparison to `metrics_summary.csv`.
* Divided the final testing properties into five actual-sale-price quintiles.
* Evaluated XGBoost performance separately across each price band.
* Compared dollar-based and percentage-based errors across market segments.
* Examined systematic overprediction and underprediction by price range.
* Identified the housing-market segments where the final model performs best and where prediction errors are largest.

## Week 8 Highlights

Expanded evaluation showed that model accuracy varies across different portions of the California housing market.

- XGBoost remains the strongest overall model with an **R² of 0.9024**, **MAPE of 12.23%**, and **MdAPE of 8.46%**.
- The **Lower-Middle Price** band (approximately **$576,000–$800,000**) achieved the strongest relative accuracy, with a **MAPE of 9.77%** and **MdAPE of 6.68%**.
- The **Lowest Price** band (**$190,000–$575,000**) produced the smallest dollar errors, with an **MAE of $58,109** and **RMSE of $94,968**.
- Dollar prediction errors increased substantially as home prices increased.
- The **Highest Price** band (approximately **$1.65 million and above**) produced the largest dollar errors, with an **MAE of $412,677** and **RMSE of $610,061**.
- The model tended to underpredict the highest-priced homes by approximately **$193,703 on average**.
- These results demonstrate why AVM performance should be evaluated across multiple metrics and market segments rather than relying on R² alone.

---

## Dataset

The underlying California MLS property datasets are proprietary and are **not included** in this public repository.

This repository contains only my source code, notebooks, documentation, and supporting materials.

---

## Modeling Notes

The prediction target for this project is:

* **ClosePrice**

Following project guidance, variables that would introduce target leakage are excluded from model training. These include:

* ListPrice
* OriginalListPrice

The project uses a chronological **training / validation / testing** framework so that model development reflects a realistic future-prediction setting.

- The training period is used to fit candidate models.
- May 2026 is reserved as the validation period for model development and hyperparameter selection.
- June 2026 is reserved as the final testing period.
- Hyperparameter decisions are made without using the final testing dataset.
- After model selection, the selected configuration is retrained using the combined training and validation data before final testing.

---

## Future Work

Future project stages will include:

* Optional Streamlit prediction application
* Final project documentation
* Presentation preparation
* Final model interpretation and project conclusions
* Repository cleanup and handoff

---

## License

This project is licensed under the MIT License.
