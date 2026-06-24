# 🌪️ Disaster Management Analytics Platform

> Analyzing historical disaster data to uncover vulnerability patterns, resource gaps, and risk trends across countries and regions globally — powered by Python, SQL, Power BI, and Streamlit.

---

## 📌 Problem Statement

Natural disasters cause massive loss of life and economic damage every year. This project aims to analyze historical disaster data to answer critical questions:

- Which countries and regions are most vulnerable to disasters?
- Which disaster types cause maximum deaths and economic loss?
- What are the trends over the years?
- How many people are affected on average?
- Which areas need more emergency resources?

---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Data Analysis | Python (Pandas, NumPy, Matplotlib, Seaborn) |
| Database | MySQL |
| Dashboard | Power BI |
| Web App | Streamlit |
| Version Control | GitHub |
| Dataset Source | Kaggle |

---

## 📁 Project Structure

```
Disaster-Management-Analytics/
│
├── data/
│   ├── disaster_raw.csv
│   └── disaster_cleaned.csv
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   └── eda.ipynb
│
├── sql/
│   └── disaster_queries.sql
│
├── dashboard/
│   ├── disaster_dashboard.pbix
│   └── dashboard_screenshots/
│       ├── overview_dashboard.png
│       └── impact_dashboard.png
│
├── app/
│   └── streamlit_app.py
│
├── images/
│   ├── disaster_types.png
│   ├── yearly_trend.png
│   ├── top_countries.png
│   └── heatmap.png
│
├── reports/
│   └── insights.md
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🗺️ Project Phases

### 🟩 Phase 1 — Problem Understanding
- Define objectives and scope
- Identify key questions to answer
- Document technologies and approach

**Status:** ✅ Complete

---

### 🟨 Phase 2 — Dataset Collection
- Source historical disaster data from Kaggle
- Key columns: Year, Country, Region, Continent, Disaster Type, Deaths, Injured, Affected Population, Economic Loss

**Status:** ✅ Complete

---

### 🟦 Phase 3 — Data Cleaning
- Remove duplicates and handle missing values
- Standardize country and region names
- Feature engineering: Severity levels, Decade grouping

**Status:** ✅ Complete

---

### 🟧 Phase 4 — Exploratory Data Analysis
- Most common disaster types (Bar chart)
- Year-wise trend (Line plot)
- Top affected countries (Horizontal bar)
- Economic loss by country (Pie chart)
- Correlation heatmap (Deaths vs Injured vs Affected Population)

**Status:** ✅ Complete

---

### 🟥 Phase 5 — SQL Database & Analytics
- Create `disaster_db` MySQL database
- Import cleaned data
- Run analytical queries: top countries, highest deaths, economic loss by country

**Status:** ✅ Complete

---

### 🟫 Phase 6 — Power BI Dashboard

**Overview Dashboard**
- KPI Cards: Total Disasters, Deaths, Injured, Population Affected, Economic Loss
- Disaster Trend (Year-wise line chart)
- Top Countries by Disaster Count (Bar chart)
- Severity Distribution (Donut chart)

**Impact Analysis Dashboard**
- Death Analysis (Stacked column chart)
- Economic Loss Analysis (Treemap)
- Global Disaster Map
- Slicers: Year, Country, Disaster Type

**Status:** ✅ Complete

---

### 🟪 Phase 7 — Insight Generation
- Identify top disaster types by frequency and impact
- Highlight most vulnerable countries and regions
- Summarize key findings in `reports/insights.md`

**Status:** ✅ Complete

---

### 🔵 Phase 8 — Streamlit Web Application
- Home: KPI overview
- Country Analysis: Filter by country
- Disaster Analysis: Filter by type
- Trends: Year-wise graphs
- Download: Export CSV/PDF report

**Status:** ✅ Complete

---

### 🟡 Phase 9 — Advanced Features
- Risk Score calculation: `Deaths×0.4 + Affected Population×0.3 + Economic Loss×0.3`
- Classify regions: Low / Medium / High Risk
- Forecasting future disaster counts
- Geographical heatmap using Folium
- PDF Report Generator

**Status:** ✅ Complete

---

### 🟠 Phase 10 — Deployment
- Deploy Streamlit app publicly
- Add screenshots, architecture diagram, and business insights

**Status:** ✅ Complete

---

## 📊 Progress Tracker

| Phase | Description | Status |
|---|---|---|
| 1 | Problem Understanding | ✅ Complete |
| 2 | Dataset Collection | ✅ Complete |
| 3 | Data Cleaning | ✅ Complete |
| 4 | Exploratory Data Analysis | ✅ Complete |
| 5 | SQL Database & Analytics | ✅ Complete |
| 6 | Power BI Dashboard | ✅ Complete |
| 7 | Insight Generation | ✅ Complete |
| 8 | Streamlit Web Application | ✅ Complete |
| 9 | Advanced Features | ✅ Complete |
| 10 | Deployment | ✅ Complete |

---

## 📸 Dashboard Screenshots

### Overview Dashboard
![Overview](dashboard/dashboard_screenshots/overview_dashboard.png)

### Impact Analysis Dashboard
![Impact](dashboard/dashboard_screenshots/impact_dashboard.png)

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```

### Run the Streamlit App

```bash
python -m streamlit run app/app.py
```

---

## 📦 Requirements

```
pandas
numpy
matplotlib
seaborn
streamlit
folium
mysql-connector-python
fpdf
scikit-learn
```

---

## 🙋 Author

**Siva Sivakumar**
- GitHub: [@siva252005](https://github.com/siva252005)
- LinkedIn: [sivasivakumar252005](https://www.linkedin.com/in/sivasivakumar252005)

---

> ⭐ Star this repo if you find it useful! Contributions and feedback are welcome.