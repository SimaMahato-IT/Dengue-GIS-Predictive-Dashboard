# Climate-Driven Dengue Epidemic Forecasting Dashboard

An end-to-end Data Science and Geospatial Analytics web application designed to predict and stratify future Dengue epidemic outbreak risks (2025–2028) based on predictive macro-environmental and climatic variations.

## 🚀 Live Demo
Access the live interactive application here: **https://dengue-gis-predictive-dashboard-xbjj3w8bbivhthkptc96ih.streamlit.app/**

---

## 📌 Project Overview
Dengue virus transmission is heavily sensitive to environmental factors. This project leverages historical epidemiological records alongside dynamic climatic parameters to forecast risk corridors across distinct zones. 

By marrying machine learning forecasts with **Spatio-Temporal GIS Mapping**, the dashboard translates complex mathematical indices into actionable, micro-administrative visualizations for health monitoring committees and local governance.

---

## 🛠️ Key Project Architecture

### 1. Predictive Backend Pipeline (Machine Learning)
* **Algorithm:** Random Forest Classification and Regression Framework.
* **Core Logic:** Uses an ensemble of Decision Trees to prevent overfitting on highly seasonal weather configurations. It processes complex environmental arrays using majority voting mechanisms.
* **Feature Engineering Vectors:** * Maximum/Minimum Ambient Temperature ($^\circ$C)
  * Cumulative Precipitation Metrics (Rainfall depth in mm)
  * Surface Moisture Indices
* **Evaluation Matrix:** Achieved an overall validation classification pipeline accuracy bounded between **86% - 88%** with a consistent trend predictability baseline ($R^2 \approx 0.81$).

### 2. Frontend Interface & Interactive GIS Layout
* **Dashboard Engine:** Built completely using the **Streamlit Web Framework**, working on reactive state management loops.
* **Spatio-Temporal Stratification Maps:** Renders fully decoupled, micro-regional interactive geospatial maps (`.html` layer matrices) categorized into distinct alert layers:
  * 🔴 **Red Zone:** Immediate Epidemic Outbreak Proximity Alert (Critical Priority)
  * 🟡 **Yellow Zone:** Preventative Surveillance Window (Moderate Warning)
  * 🟢 **Green Zone:** Safe Ecological Baseline (Standard Containment)

### 3. Deep-Dive Administrative Analytics Grid
* Integrated deep historical and multi-year trajectory timeline filter panels.
* Features a micro-administrative audit dataset enabling localized city/state case tracking.
* Built-in downstream target serialization supporting real-time **Excel/CSV data downloads** for localized epidemic contingency drafting.

---

## 📂 Repository File System Structure
```text
├── app.py                         
├── requirements.txt               
├── dengue_discrete_zones_2025.html 
├── dengue_discrete_zones_2026.html 
├── dengue_discrete_zones_2027.html 
├── dengue_discrete_zones_2028.html 
└── README.md             
