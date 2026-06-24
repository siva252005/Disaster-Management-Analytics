import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Disaster Management Analytics",
    page_icon="🌍",
    layout="wide"
)

# Title
st.title("🌍 Disaster Management Analytics Platform")

# Introduction
st.markdown("""
### Welcome!

This project analyzes historical disaster data from **1970–2021** to understand:

- 🌪 Disaster trends
- ☠ Human impact
- 💰 Economic losses
- 🌎 Geographical distribution
- 📊 Key insights for disaster management

---

### 📌 Available Dashboards

#### 📊 Overview Dashboard
- KPI Cards
- Disaster Trends
- Top Countries
- Severity Distribution

#### ☠ Impact Analysis Dashboard
- Death Analysis
- Economic Loss Analysis
- Global Disaster Map

Use the sidebar to navigate between pages.
""")

st.success("Phase 9 - Streamlit Application Started Successfully 🚀")