# 🏠 Real Estate Automated Valuation Model (AVM) Dashboard

A web-based Machine Learning application built using **Streamlit** to predict property market sales values in AUD. This interactive dashboard bridges the gap between statistical modeling and business application, allowing end-users to input structural property features and receive instantaneous valuation estimations.

🔗 **[[(https://streamlit.io](https://property-valuation-dashboard-2m3gafcdfzh9xaxwlsnnzt.streamlit.app/)]** 

---

## 🎯 Project Overview & Objective
The goal of this project was to transition a raw real estate analytics workflow from an exploratory sandbox into a secure, production-grade cloud dashboard. The model evaluates property parameters across key Australian suburbs to calculate custom localized pricing variations.

### Core App Parameters:
*   **Suburb Locations:** Sydney, Marrickville, Blacktown
*   **Property Natures:** Apartment, House
*   **Continuous Features:** Size in square meters ($m^2$), Bedrooms, Bathrooms, Car Spaces

---

## 🛠️ Data Science Pipeline & Feature Engineering
Before generating predictions, the underlying system translates human-readable metrics into a structured sparse matrix using advanced feature engineering pipelines tested within the parent Jupyter Notebook (`.ipynb`).

### 1. Categorical Dummy Encoding
To feed non-numeric text variables into our machine learning algorithms, categorical metrics are systematically transformed. The system handles alphabetical lists and drops the baseline category reference string (`Blacktown`) to fully mitigate spatial multicollinearity risks:
$$\text{Suburb} \rightarrow [\text{Suburb\_Marrickville}, \text{Suburb\_Sydney}]$$

### 2. Custom Location Interaction Terms
Real estate pricing changes dramatically based on location tier structures. To allow factors like *price per square meter* to shift dynamically based on geographic code matrices, custom cross-product interaction terms were explicitly mapped into the feature vector space:
*   `Size_x_Suburb_Sydney` = `Size in sq meter` $\times$ `Suburb_Sydney`
*   `Bed_x_Suburb_Sydney` = `Bed room` $\times$ `Suburb_Sydney`

---

## 🚀 Cloud Architecture & Deployment Workarounds
The application is containerized and hosted natively using **Streamlit Community Cloud** tied directly to version-controlled updates on GitHub. 

### Overcoming Platform Version Constraints
During deployment, standard serialization libraries (`joblib`/`scikit-learn`) encountered environment version conflicts due to a cloud platform edge condition running experimental Python versions. 

To overcome this, a production-grade **algorithmic engine reconstruction fallback script** was developed. By mathematical extraction of the trained tree boundaries and core coefficient scales directly into a localized pure-Python prediction matrix, the application achieved:
1.  **Zero External Dependencies:** Removed version-locked module vulnerabilities (`ModuleNotFoundError`).
2.  **Blazing Fast Execution Speed:** Completely eliminated disk reading I/O times required to deserialize binary `.pkl` files.
3.  **High Stability:** Bulletproof processing against system updates or cross-platform package corruption.

---

## 💻 Local Workspace Execution Setup
To review the interface execution logic locally on your computer terminal workspace, run the following steps:

1. Clone the project repository:
   ```bash
   git clone https://github.com
   cd property-valuation-dashboard
   ```

2. Run the application using Python's active module execution flags:
   ```bash
   python -m streamlit run streamlit_app.py
   ```

---

## 📊 Technologies Used
*   **Core Logic:** Python 3.11+, NumPy, Pandas
*   **Statistical Modeling Source:** Scikit-Learn, Joblib, Jupyter Notebooks
*   **Web Framework & UI Container:** Streamlit Cloud Architecture
*   **Version Control:** Git & GitHub Respositories
