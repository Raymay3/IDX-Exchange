# ============================================
# Import required libraries
# ============================================

import streamlit as st
import pandas as pd
import joblib

# ============================================
# Load the trained XGBoost model
# ============================================

model = joblib.load("model.pkl")

preprocessing = joblib.load("preprocessing.pkl")

scaler = preprocessing["scaler"]
district_target_map = preprocessing["district_target_map"]
global_mean_price = preprocessing["global_mean_price"]
continuous_columns = preprocessing["continuous_columns"]

# ============================================
# Configure the Streamlit page
# ============================================

st.set_page_config(
    page_title="California Home Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# ============================================
# Display the application title
# ============================================

st.title("🏠 California Home Price Predictor")

st.markdown(
    """
    Estimate the sale price of a California
    single-family home using a trained
    XGBoost machine learning model.
    """
)

# ============================================
# Display model information
# ============================================

with st.sidebar:

    st.header("About")

    st.markdown(
        """
California Home Price Predictor

**Machine Learning Model:**
- Tuned XGBoost Regressor

**Dataset:**
- California CRMLS Single-Family Residential Sales
- January 2022 – June 2026

**Project:**
- Built during the IDX Exchange
  Data Science Internship (2026)
        """
    )

st.divider()

# ============================================
# Property information
# ============================================

st.header("Property Information")

col1, col2 = st.columns(2)

with col1:
    living_area = st.number_input(
        "Living Area (sq ft)",
        min_value=100,
        value=2000
    )

with col2:
    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        value=3
    )

with col1:
    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        value=2
    )

with col2:
    lot_size = st.number_input(
        "Lot Size (sq ft)",
        min_value=500,
        value=7000
    )

with col1:
    garage_spaces = st.number_input(
        "Garage Spaces",
        min_value=0,
        value=2
    )

with col2:
    parking_spaces = st.number_input(
        "Parking Spaces",
        min_value=0,
        value=2
    )

with col1:
    stories = st.selectbox(
        "Stories",
        [
            "One",
            "Two",
            "ThreeOrMore"
        ]
    )

with col2:
    property_age = st.number_input(
        "Property Age",
        min_value=0,
        value=25
    )

association_fee = st.number_input(
    "Association Fee ($)",
    min_value=0,
    value=0
)

county_options = sorted([
    column.replace("CountyOrParish_", "")
    for column in model.feature_names_in_
    if column.startswith("CountyOrParish_")
])

county = st.selectbox(
    "County",
    county_options
)

district_options = sorted(district_target_map.index)

school_district = st.selectbox(
    "School District",
    district_options
)

fireplace = st.checkbox("Fireplace")

pool = st.checkbox("Private Pool")

attached_garage = st.checkbox("Attached Garage")

new_construction = st.checkbox("New Construction")

st.divider()

# ============================================
# Predict home price
# ============================================

if st.button(
    "🏠 Predict Home Price",
    use_container_width=True
):

    # Create one empty row using every feature
    # expected by the trained XGBoost model.
    input_data = pd.DataFrame(
        0.0,
        index=[0],
        columns=model.feature_names_in_
    )

    # ============================================
    # Populate the core property features
    # ============================================

    input_data.loc[0, "LivingArea"] = living_area
    input_data.loc[0, "BedroomsTotal"] = bedrooms
    input_data.loc[0, "BathroomsTotalInteger"] = bathrooms
    input_data.loc[0, "LotSizeSquareFeet"] = lot_size
    input_data.loc[0, "LotSizeArea"] = lot_size
    input_data.loc[0, "GarageSpaces"] = garage_spaces
    input_data.loc[0, "ParkingTotal"] = parking_spaces
    input_data.loc[0, "AssociationFee"] = association_fee
    input_data.loc[0, "PropertyAge"] = property_age

    # ============================================
    # Calculate engineered features
    # ============================================

    input_data.loc[0, "BathroomBedroomRatio"] = (
        bathrooms / bedrooms
        if bedrooms > 0 else 0
    )

    input_data.loc[0, "LivingAreaPerBedroom"] = (
        living_area / bedrooms
        if bedrooms > 0 else 0
    )

    input_data.loc[0, "LotSizePerLivingArea"] = (
        lot_size / living_area
        if living_area > 0 else 0
    )

    # ============================================
    # Populate the boolean property features
    # ============================================

    input_data.loc[0, "FireplaceYN_True"] = int(fireplace)
    input_data.loc[0, "PoolPrivateYN_True"] = int(pool)
    input_data.loc[0, "AttachedGarageYN_True"] = int(attached_garage)
    input_data.loc[0, "NewConstructionYN_True"] = int(new_construction)

    # ============================================
    # Populate the county feature
    # ============================================

    county_column = f"CountyOrParish_{county}"

    if county_column in input_data.columns:
        input_data.loc[0, county_column] = 1.0

    # ============================================
    # Populate the school district feature
    # ============================================

    if school_district in district_target_map.index:
        district_value = district_target_map[school_district]
    else:
        district_value = global_mean_price

    input_data.loc[0, "DistrictName_TE"] = district_value

    # ============================================
    # Populate the levels feature
    # ============================================

    levels_column = f"Levels_{stories}"

    if levels_column in input_data.columns:
        input_data.loc[0, levels_column] = 1.0

    # ============================================
    # Scale the continuous features
    # ============================================

    input_data[continuous_columns] = scaler.transform(
        input_data[continuous_columns]
    )

    # ============================================
    # Predict the home price
    # ============================================

    try:

        with st.spinner("Estimating home price..."):

            prediction = model.predict(input_data)

        predicted_price = prediction[0]

        st.metric(
            label="Estimated Home Price",
            value=f"${predicted_price:,.0f}"
        )

        st.caption(
            """
            This estimate is based on the information provided.
            Some model features that are not collected in this demo
            (such as precise location and street number)
            are assigned default values.
            """
        )

    except Exception as e:

        st.error(f"Prediction failed: {e}")


st.divider()

st.caption(
    "Developed by Gabriella Gass • IDX Exchange Data Science Internship • 2026"
)