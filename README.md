# 🌪️ Disaster Management Analytics Platform

> Analyzing historical disaster data to uncover vulnerability patterns, resource gaps, and risk trends across India — powered by Python, SQL, Power BI, and Streamlit.

---

## 📌 Problem Statement

Natural disasters cause massive loss of life and economic damage every year. This project aims to analyze historical disaster data to answer critical questions:

- Which states are most vulnerable to disasters?
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
│   └── disaster_dashboard.pbix
│
├── app/
│   └── streamlit_app.py
│
├── images/
│   ├── disaster_types.png
│   ├── yearly_trend.png
│   ├── top_states.png
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

**Status:** 🔲 Not Started

---

### 🟨 Phase 2 — Dataset Collection
- Source historical disaster data from Kaggle
- Key columns: Year, State, District, Disaster Type, Deaths, Injured, Affected Population, Economic Loss

**Status:** 🔲 Not Started

---

### 🟦 Phase 3 — Data Cleaning
- Remove duplicates and handle missing values
- Standardize state names (e.g. `TN` → `Tamil Nadu`)
- Feature engineering: Severity levels, Decade grouping

**Status:** 🔲 Not Started

---

### 🟧 Phase 4 — Exploratory Data Analysis
- Most common disaster types (Bar chart)
- Year-wise trend (Line plot)
- Top affected states (Horizontal bar)
- Economic loss distribution (Pie chart)
- Correlation heatmap (Deaths vs Injured vs Affected Population)

**Status:** 🔲 Not Started

---

### 🟥 Phase 5 — SQL Database & Analytics
- Create `disaster_db` MySQL database
- Import cleaned data
- Run analytical queries: top states, highest deaths, economic loss by state

**Status:** 🔲 Not Started

---

### 🟫 Phase 6 — Power BI Dashboard
- KPI Cards: Total Disasters, Deaths, Injured, Population Affected, Economic Loss
- Charts: Year-wise trend, State-wise disasters, Disaster distribution, Economic loss treemap
- Slicers: Year, State, Disaster Type

**Status:** 🔲 Not Started

---

### 🟪 Phase 7 — Insight Generation
- Identify top disaster types by frequency and impact
- Highlight most vulnerable states
- Summarize key findings in `reports/insights.md`

**Status:** 🔲 Not Started

---

### 🔵 Phase 8 — Streamlit Web Application
- Home: KPI overview
- State Analysis: Filter by state
- Disaster Analysis: Filter by type
- Trends: Year-wise graphs
- Download: Export CSV/PDF report

**Status:** 🔲 Not Started

---

### 🟡 Phase 9 — Advanced Features
- Risk Score calculation: `Deaths×0.4 + Affected Population×0.3 + Economic Loss×0.3`
- Classify regions: Low / Medium / High Risk
- Forecasting future disaster counts
- Geographical heatmap using Folium
- PDF Report Generator

**Status:** 🔲 Not Started

---

### 🟠 Phase 10 — Deployment
- Deploy Streamlit app publicly
- Add screenshots, architecture diagram, and business insights

**Status:** 🔲 Not Started

---

## 📊 Progress Tracker

| Phase | Description | Status |
|---|---|---|
| 1 | Problem Understanding | 🔲 Not Started |
| 2 | Dataset Collection | 🔲 Not Started |
| 3 | Data Cleaning | 🔲 Not Started |
| 4 | Exploratory Data Analysis | 🔲 Not Started |
| 5 | SQL Database & Analytics | 🔲 Not Started |
| 6 | Power BI Dashboard | 🔲 Not Started |
| 7 | Insight Generation | 🔲 Not Started |
| 8 | Streamlit Web Application | 🔲 Not Started |
| 9 | Advanced Features | 🔲 Not Started |
| 10 | Deployment | 🔲 Not Started |

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```

### Run the Streamlit App (once complete)

```bash
streamlit run app/streamlit_app.py
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

**[Your Name]**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

> ⭐ Star this repo if you find it useful! Contributions and feedback are welcome.
