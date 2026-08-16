import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# =====================================================================
# 1. GRAPHICAL INTERFACE SETUP & ARTIFACT DESERIALIZATION
# =====================================================================
st.set_page_config(
    page_title="Property Pricing Dashboard",
    page_icon="🏠",
    layout="centered"
)

@st.cache_resource
def load_ml_model():
    """Loads the trained Random Forest model object artifact safely from disk."""
    model_path = "model.pkl"
    if os.path.exists(model_path):
        return joblib.load(model_path), False
    return None, True

rf_model, is_simulation = load_ml_model()

# --- HARDCODED MODEL FEATURE COLUMNS MATRIX ---
features = [
    'Size in sq meter', 'Bed room', 'Shower', 'Car spaces',
    'Suburb_Marrickville', 'Suburb_Sydney', 
    'Nature_House',
    'Size_x_Suburb_Marrickville', 'Bed_x_Suburb_Marrickville',
    'Size_x_Suburb_Sydney', 'Bed_x_Suburb_Sydney'
]

# Dropdown list selections for user mapping interface
KNOWN_SUBURBS = ["Sydney", "Marrickville", "Blacktown"]
KNOWN_NATURES = ["Apartment", "House"]

# =====================================================================
# 2. CORE PRODUCTION ENGINE: DYNAMIC ALIGNMENT & PREDICTION
# =====================================================================
def predict_property_price(suburb, nature, size, bedrooms, showers, car_spaces):
    """
    Accepts raw property metrics, replicates dummy columns, automatically
    calculates interaction features, and returns a Random Forest prediction.
    """
    model_features = features 
    
    new_house_dict = {
        'Size in sq meter': float(size),
        'Bed room': int(bedrooms),
        'Shower': int(showers),
        'Car spaces': int(car_spaces)
    }
    
    for col in model_features:
        if col not in new_house_dict:
            new_house_dict[col] = 0.0
            
    target_suburb_col = f"Suburb_{suburb}"
    target_nature_col = f"Nature_{nature}"
    
    if target_suburb_col in new_house_dict:
        new_house_dict[target_suburb_col] = 1.0
        
    if target_nature_col in new_house_dict:
        new_house_dict[target_nature_col] = 1.0
        
    for col in model_features:
        if '_x_Suburb_' in col:
            if col.endswith(suburb):
                if col.startswith('Size_x_'):
                    new_house_dict[col] = float(size)
                elif col.startswith('Bed_x_'):
                    new_house_dict[col] = float(bedrooms)
            else:
                new_house_dict[col] = 0.0

    input_df = pd.DataFrame([new_house_dict])[model_features]
    predicted_price = rf_model.predict(input_df)
    return float(predicted_price[0])


# =====================================================================
# 3. USER INTERFACE DESIGN LAYOUT (STREAMLIT WIDGETS)
# =====================================================================
st.title("🏠 Automated Property Valuation Engine")
st.markdown("Input property characteristics below to generate a real-time price estimation from your Random Forest model.")

if is_simulation:
    st.error("🚨 **`model.pkl` Object Missing!** Ensure your model object file is correctly uploaded to your repository.")

with st.form("valuation_form"):
    st.subheader("📋 Property Metric Matrix Configuration")
    
    col1, col2 = st.columns(2)
    with col1:
        suburb_input = st.selectbox("Select Suburb Location", KNOWN_SUBURBS)
        size_input = st.number_input("Size in Square Meters (m²)", min_value=10, max_value=5000, value=120, step=5)
        showers_input = st.number_input("Number of Bathrooms / Showers", min_value=1, max_value=10, value=2, step=1)
    
    with col2:
        nature_input = st.selectbox("Select Property Nature", KNOWN_NATURES)
        bedrooms_input = st.number_input("Number of Bedrooms", min_value=1, max_value=15, value=3, step=1)
        car_spaces_input = st.number_input("Number of Car Spaces", min_value=0, max_value=10, value=1, step=1)

    submit_button = st.form_submit_button(label="🔮 Calculate Estimated Market Price")

if submit_button:
    if is_simulation:
        st.warning("Prediction calculation failed because your model file is missing.")
    else:
        try:
            with st.spinner("Processing feature telemetry profiles through ML model matrix..."):
                valuation = predict_property_price(
                    suburb=suburb_input, 
                    nature=nature_input, 
                    size=size_input, 
                    bedrooms=bedrooms_input, 
                    showers=showers_input, 
                    car_spaces=car_spaces_input
                )
            
            st.success("### Calculation Finalized Successfully!")
            st.metric(
                label="Estimated Market Value (AUD)", 
                value=f"${valuation:,.2f} AUD"
            )
            
        except Exception as e:
            st.error(f"❌ Valuation Pipeline Error: {str(e)}")
