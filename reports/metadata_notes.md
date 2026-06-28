# Metadata Notes

## Week 1 Deliverable

### Dataset Access

Successfully connected to the IDX Exchange data source and downloaded more than the required six months of California CRMLS sold-property datasets for local analysis. The datasets were reviewed to verify accessibility and consistency across multiple monthly files.

The underlying MLS datasets are proprietary and are therefore not included in this public repository.

---

## Primary Target Variable

### ClosePrice

The final sale price of the property. This is the prediction target for the machine learning models developed during the internship.

---

## Key Property Features

### LivingArea

Finished interior living area of the property (square feet). Expected to be one of the strongest predictors of sale price.

### BedroomsTotal

Total number of bedrooms.

### BathroomsTotalInteger

Total number of bathrooms.

### LotSizeAcres

Lot size of the property.

### YearBuilt

Year the home was constructed. Can be used to derive property age.

### PropertyType

General property classification.

Only observations where:

* PropertyType = Residential

will be retained.

### PropertySubType

More specific property classification.

Only observations where:

* PropertySubType = SingleFamilyResidence

will be used for model development.

---

## Location Features

### Latitude

Latitude coordinate of the property.

### Longitude

Longitude coordinate of the property.

### CountyOrParish

County in which the property is located.

### MLSAreaMajor

MLS market area identifier.

---

## Additional Candidate Features

* DaysOnMarket
* ParkingTotal
* FireplacesTotal
* TaxAnnualAmount
* ElementarySchool
* MiddleOrJuniorSchool
* HighSchool

These variables may be evaluated during feature selection and model development.

---

## Variables Excluded from Modeling

### ListPrice

Excluded due to target leakage.

### OriginalListPrice

Excluded due to target leakage.

Per project guidance, these variables will not be used as model features because they can artificially inflate predictive performance.

---

## Notes

The dataset structure was reviewed across multiple monthly CRMLS files from 2024–2026. The schema is highly consistent between months, allowing the same preprocessing pipeline to be applied throughout the project.
