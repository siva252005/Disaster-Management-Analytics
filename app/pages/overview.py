import streamlit as st
import pandas as pd
import plotly.express as px

# Load CSS
def load_css():
    with open("app/assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# Page Config
st.set_page_config(
    page_title="Overview Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Disaster Management Analytics - Overview Dashboard")

# Load Data
df = pd.read_csv("data/processed/disaster_cleaned.csv")

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("Filters")

selected_continent = st.sidebar.multiselect(
    "Continent",
    options=df["Continent"].unique(),
    default=df["Continent"].unique()
)

selected_disaster = st.sidebar.multiselect(
    "Disaster Type",
    options=df["Disaster_Type"].unique(),
    default=df["Disaster_Type"].unique()
)

selected_year = st.sidebar.slider(
    "Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (int(df["Year"].min()), int(df["Year"].max()))
)

# Filter Data
filtered_df = df[
    (df["Continent"].isin(selected_continent))
    & (df["Disaster_Type"].isin(selected_disaster))
    & (df["Year"].between(selected_year[0], selected_year[1]))
]

# ---------------- DOWNLOAD BUTTON ----------------
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv,
    file_name="filtered_disaster_data.csv",
    mime="text/csv"
)

# ---------------- KPI CARDS ----------------
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Disasters", len(filtered_df))
col2.metric("Total Deaths", int(filtered_df["Deaths"].sum()))
col3.metric("Total Affected", int(filtered_df["Total_Affected"].sum()))
col4.metric("Economic Loss", f"${int(filtered_df['Total_Damages_USD'].sum()):,}")
col5.metric("Countries", filtered_df["Country"].nunique())

# ---------------- TREND CHART ----------------
yearly = filtered_df.groupby("Year").size().reset_index(name="Count")

fig1 = px.line(
    yearly,
    x="Year",
    y="Count",
    markers=True,
    title="Disaster Trend (1970-2021)"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------- CHARTS ----------------
col1, col2 = st.columns(2)

# Disaster Type Distribution
with col1:
    disaster_count = (
        filtered_df["Disaster_Type"]
        .value_counts()
        .reset_index()
    )
    disaster_count.columns = ["Disaster Type", "Count"]

    fig2 = px.bar(
        disaster_count,
        x="Disaster Type",
        y="Count",
        title="Disaster Type Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

# Top Countries
with col2:
    top_country = (
        filtered_df["Country"]
        .value_counts()
        .head(10)
        .reset_index()
    )
    top_country.columns = ["Country", "Count"]

    fig3 = px.bar(
        top_country,
        x="Country",
        y="Count",
        title="Top 10 Countries by Disaster Count"
    )

    st.plotly_chart(fig3, use_container_width=True)

# ---------------- SEVERITY DISTRIBUTION ----------------
severity = filtered_df["Severity"].value_counts().reset_index()
severity.columns = ["Severity", "Count"]

fig4 = px.pie(
    severity,
    names="Severity",
    values="Count",
    title="Severity Distribution"
)

st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

st.markdown("""
### 👨‍💻 Developed By

**Siva S**

- B.Tech Artificial Intelligence & Data Science
- Sri Shakthi Institute of Engineering and Technology
- Data Analytics Enthusiast
""")