# Data

The California Regional Multiple Listing Service (CRMLS) Sold datasets used in this project are proprietary and are **not included in this public repository**.

The raw data consists of monthly `CRMLSSold` CSV files containing historical California property transaction records and property characteristics.

## Expected Data Structure

To reproduce the analysis, authorized users should place the monthly CRMLS Sold CSV files inside the `data/California/` directory:

```text
data/
├── README.md
└── California/
    ├── CRMLSSold202201.csv
    ├── CRMLSSold202202.csv
    ├── ...
    └── CRMLSSold202606.csv
```

The exploration and preprocessing notebooks automatically locate and combine the CSV files stored in `data/California/`.

## Generated Data Files

Running the preprocessing notebook creates the cleaned datasets used by the modeling notebooks:

```text
data/
├── train_cleaned.csv
├── validation_cleaned.csv
└── test_cleaned.csv
```

These generated datasets are also excluded from the public repository because they are derived from the proprietary CRMLS data.

## Reproducing the Project

Authorized users should:

1. Place the monthly CRMLS Sold CSV files in `data/California/`.
2. Run `01_exploration.ipynb` for exploratory data analysis.
3. Run `02_preprocessing.ipynb` to generate the cleaned training, validation, and testing datasets.
4. Continue with the remaining modeling notebooks in numerical order.
