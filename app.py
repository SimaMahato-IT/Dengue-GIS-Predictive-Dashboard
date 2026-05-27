import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import os

# 1. Production-Grade Environment Master Setup
st.set_page_config(
    page_title="Dengue Spatio-Temporal GIS System",
    page_icon="🦟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Main Navigation Pipeline
st.sidebar.title("📌 Navigation Panel")
app_mode = st.sidebar.radio(
    "Go To Workspace Page:",
    ["🏠 Executive Summary", "🗺️ Spatio-Temporal GIS Risk Map", "📊 Regional Analytics Matrix"]
)

st.sidebar.write("---")

# Global Analytical Core Data Arrays (Calibrated from Spatial Logs)
years_axis = ['2025', '2026', '2027', '2028']
risk_trend_matrix = pd.DataFrame({
    '🔴 High Risk (Red)': [446, 1016, 1275, 1542],
    '🟡 Medium Risk (Yellow)': [625, 2578, 3296, 3478],
    '🟢 Safe Baseline (Green)': [6055, 3532, 2555, 2106]
}, index=years_axis)

# Hotspot Matrix Dictionary (2025 - 2028) for Tabular & Chart Render
hotspot_master_registry = {
    2025: {
        "City_Name": ["delhi", "mumbai", "chennai", "kolkata", "bangalore", "hyderabad", "pune", "ahmedabad", "jaipur", "lucknow"],
        "Predicted_Cases": [520, 480, 410, 395, 310, 290, 275, 240, 195, 180]
    },
    2026: {
        "City_Name": ["bangalore", "mysore", "mangalore", "belgaum", "hubli", "gulbarga", "bellary", "bijapur", "shimoga", "bidar"],
        "Predicted_Cases": [1420, 1280, 1150, 980, 890, 810, 760, 710, 640, 590]
    },
    2027: {
        "City_Name": ["gadag", "tumkur", "udupi", "chikmagalur", "mandya", "bangalore", "bijapur", "mysore", "kolar", "hassan"],
        "Predicted_Cases": [3450, 3210, 3180, 2950, 2800, 2750, 2600, 2450, 2100, 1950]
    },
    2028: {
        "City_Name": ["gadag", "chikmagalur", "udupi", "tumkur", "bangalore", "bijapur", "mandya", "mysore", "bellary", "chitradurga"],
        "Predicted_Cases": [6107, 6048, 6041, 6041, 6037, 6037, 6023, 6023, 5890, 5740]
    }
}

# ==========================================
# PAGE 1: EXECUTIVE SUMMARY
# ==========================================
if app_mode == "🏠 Executive Summary":
    st.title("🦟 Climate-Driven Dengue Epidemic Forecasting Dashboard")
    st.markdown("### Hybrid Machine Learning & Spatio-Temporal GIS Risk Stratification (2025 - 2028)")
    st.write("---")
    
    col1, col2 = st.columns([4, 5])
    
    with col1:
        st.markdown("#### 📝 Project Strategic Overview")
        st.write("""
        Yeh platform advanced predictive modeling aur geographic information systems (GIS) ko merge karke 
        micro-climate fluctuations (Temperature, Precipitation, Surface parameters) ke basis par agle 4 saal ka 
        Dengue Outbreak Risk map karta hai.
        
        **Key Project Dimensions:**
        * **Predictive Framework:** Random Forest Regression/Classification Pipeline.
        * **Spatio-Temporal Horizon:** Multi-year target indexing (2025 - 2028).
        * **Risk Classification:** Stratified into Discrete Zones based on empirical incident density.
        """)
        
    with col2:
        st.markdown("#### 📉 Multi-Year Risk Distribution Timeline Trends")
        # Fixed: Changed to line_chart so the red risk line isn't compressed at the bottom layer
        st.line_chart(risk_trend_matrix, color=["#FF4B4B", "#FFA500", "#2E7D32"], height=360)
        st.caption("📈 Graph: Spatio-temporal line intersections showing a clear escalation in High Risk zones alongside falling Safe Baselines.")
        
    st.write("---")
    # Fixed: Green success text notification note removed from here completely for clean UI.

# ==========================================
# PAGE 2: SPATIO-TEMPORAL GIS RISK MAP
# ==========================================
elif app_mode == "🗺️ Spatio-Temporal GIS Risk Map":
    st.title("🗺️ Interactive Geospatial Boundary Maps")
    st.markdown("### Discrete Risk Stratification and Epidemiological Buffer Layouts")
    st.write("---")
    
    st.sidebar.subheader("🕹️ Layer Controller")
    selected_year = st.sidebar.selectbox(
        "Select Forecasting Year Horizon:",
        [2025, 2026, 2027, 2028],
        index=3
    )

    st.sidebar.markdown("""
    **💡 Standard UI Legend Matrix:**
    * 🔴 **Red Zone:** Outbreak Alert Critical
    * 🟡 **Yellow Zone:** Warning Monitoring Sectors
    * 🟢 **Green Zone:** Safe Baseline Stable Regions
    """)

    st.subheader(f"📊 Projected Epidemiological Risk Mapping for Year {selected_year}")
    map_file_path = f"dengue_discrete_zones_{selected_year}.html"

    col1, col2 = st.columns([3, 1])

    with col1:
        if os.path.exists(map_file_path):
            st.markdown(f"**Interactive GIS Spatial Boundary Map Layer ({selected_year})**")
            with open(map_file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            components.html(html_content, height=550, scrolling=True)
        else:
            st.error(f"❌ Target File '{map_file_path}' not found in current directory.")

    with col2:
        st.markdown("#### 📢 Regional Risk Matrix")
        if selected_year == 2025:
            st.metric(label="🔴 Outbreak Zones (Red)", value="446")
            st.metric(label="🟡 Warning Zones (Yellow)", value="625")
            st.metric(label="🟢 Safe Zones (Green)", value="6,055")
        elif selected_year == 2026:
            st.metric(label="🔴 Outbreak Zones (Red)", value="1,016")
            st.metric(label="🟡 Warning Zones (Yellow)", value="2,578")
            st.metric(label="🟢 Safe Zones (Green)", value="3,532")
        elif selected_year == 2027:
            st.metric(label="🔴 Outbreak Zones (Red)", value="1,275")
            st.metric(label="🟡 Warning Zones (Yellow)", value="3,296")
            st.metric(label="🟢 Safe Zones (Green)", value="2,555")
        elif selected_year == 2028:
            st.metric(label="🔴 Outbreak Zones (Red)", value="1,542")
            st.metric(label="🟡 Warning Zones (Yellow)", value="3,478")
            st.metric(label="🟢 Safe Zones (Green)", value="2,106")

# ==========================================
# PAGE 3: REGIONAL ANALYTICS MATRIX
# ==========================================
elif app_mode == "📊 Regional Analytics Matrix":
    st.title("📊 Micro-Administrative Metrics Grid")
    st.markdown("### Granular Classification Validation Ledger and Regional Data Tables")
    st.write("---")
    
    st.markdown("#### 🛠️ Deep-Dive Historical Filter Panel")
    analytics_year = st.slider("Select Horizon for Hotspot Auditing:", min_value=2025, max_value=2028, value=2028, step=1)
    
    target_data = hotspot_master_registry[analytics_year]
    df_snapshot = pd.DataFrame({
        "State_Name": ["karnataka" if analytics_year >= 2026 else "multistate"] * 10,
        "City_Name": target_data["City_Name"],
        "Predicted_Cases": target_data["Predicted_Cases"],
        "Risk_Category": ["High Risk Zone (Red Alert)"] * 10
    })
    
    col_chart, col_table = st.columns([5, 4])
    
    with col_chart:
        st.markdown(f"📊 **Top 10 High-Risk Outbreak Concentrations ({analytics_year})**")
        chart_df = pd.DataFrame({
            'Predicted Cases': target_data["Predicted_Cases"]
        }, index=target_data["City_Name"])
        st.bar_chart(chart_df, color="#D32F2F", height=320)
        
    with col_table:
        st.markdown(f"📋 **Validation Audit Sheet ({analytics_year})**")
        st.dataframe(df_snapshot, use_container_width=True, height=320)
        
    st.write("---")
    st.download_button(
        label=f"📥 Download Analytical Records for Year {analytics_year} (.CSV)",
        data=df_snapshot.to_csv(index=False),
        file_name=f"dengue_predictive_report_{analytics_year}.csv",
        mime="text/csv"
    )