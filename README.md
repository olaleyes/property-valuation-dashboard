# 🏠 Real Estate Automated Valuation Model (AVM) Engine

A web-based Machine Learning application built using **Streamlit** to predict residential property sales values in AUD. This interactive dashboard bridges the gap between statistical modeling and business application, allowing end-users to input structural property features and receive instantaneous valuation estimations.

---

## 📋 System Requirements & Prerequisite Tools
Before deploying or executing the source code, ensure your local computing environment possesses the following minimum dependencies:
*   **Operating System:** Windows 10/11, macOS, or Linux
*   **Base Language Runtime:** Python 3.11 or Python 3.12 (Highly Recommended)
*   *Note: Avoid running inside unverified Python 3.14 environments due to upstream library build package compatibility restrictions.*

---

## 🛠️ Step-by-Step Installation & Build Guide

### 1. Clone or Extract the Source Code Directory
Extract your downloaded project ZIP archive file, open your system terminal command prompt (`cmd` or terminal application), and navigate directly into the root folder:
```bash
cd "C:\Users\SAMSON\property-valuation-dashboard"
```

### 2. Configure a Clean Virtual Environment (Optional but Recommended)
To prevent package version conflicts across your global operating system directories, initialize an isolated application sandbox layer:
```bash
python -m venv venv
```
Activate the environment tracking terminal:
*   **Windows (Command Prompt):** `venv\Scripts\activate.bat`
*   **macOS / Linux:** `source venv/bin/activate`

### 3. Install Required Library Dependencies
Execute the pip installer framework to automatically resolve and download all core data science and web rendering packages defined inside the workspace registry:
```bash
python -m pip install -r requirements.txt
```

---

## 🚀 Execution & Run Protocols

To launch the graphical dashboard application interface server locally on your laptop workspace machine, run the following execution command:

```bash
python -m streamlit run streamlit_app.py
```

### Accessing the Interface Dashboard
Once the local compilation sequences finalize successfully, the system console will broadcast the server connection configurations. Open your web browser and navigate directly to the local port address:
👉 **http://localhost:8501** (or **http://localhost:8502**)

---

## 📊 Reproducing Statistical & Algorithmic Results

To replicate the original data engineering transformations and verify model consistency metrics, execute the pipeline inputs matching these controlled baseline profiles:

### 🔬 Controlled Test Profiles Matrix:

| Parameter Attribute | Baseline Evaluation Profile A | Baseline Evaluation Profile B |
| :--- | :--- | :--- |
| **Suburb Location** | `Sydney` | `Marrickville` |
| **Property Nature** | `Apartment` | `House` |
| **Size in Square Meters (\(m^2\))** | `120` | `150` |
| **Number of Bedrooms** | `3` | `4` |
| **Number of Bathrooms** | `2` | `2` |
| **Number of Car Spaces** | `1` | `2` |
| **Expected System Output** | **\$1,592,000.00 AUD** | **\$1,300,500.00 AUD** |

### Verification Methodology:
1. Open the running Streamlit web application tab in your browser.
2. Manually map the drop-down boxes and input numeric fields to match **Profile A** above.
3. Click **🔮 Calculate Estimated Market Price**.
4. Confirm that the green valuation success card outputs exactly **\$1,592,000.00 AUD**. This verifies that your local server's internal categorical encoding vectors and structural interaction multipliers match the cloud deployment baseline.

---

## 📁 Repository Directory Structure Configuration
```text
property-valuation-dashboard/
├── streamlit_app.py      # Main graphical Streamlit application engine script
├── requirements.txt      # Platform dependency version mapping definitions file
├── model.pkl             # Serialized machine learning estimator matrix artifact
└── README.md             # Complete user installation and deployment manual
```
