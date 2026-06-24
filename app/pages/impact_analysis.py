import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Overview Dashboard",
    layout="wide"
)
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
    page_title="Impact Analysis Dashboard",
    page_icon="☠️",
    layout="wide"
)

st.title("☠️ Impact Analysis Dashboard")

# Load Data
df = pd.read_csv("data/processed/disaster_cleaned.csv")

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("Filters")

selected_continent = st.sidebar.multiselect(
    "Continent",
    options=df["Continent"].unique(),
    default=df["Continent"].unique()
)

selected_severity = st.sidebar.multiselect(
    "Severity",
    options=df["Severity"].unique(),
    default=df["Severity"].unique()
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
    & (df["Severity"].isin(selected_severity))
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

# ---------------- DEATH ANALYSIS ----------------
col1, col2 = st.columns(2)

with col1:
    deaths_type = (
        filtered_df.groupby("Disaster_Type")["Deaths"]
        .sum()
        .reset_index()
        .sort_values(by="Deaths", ascending=False)
    )

    fig1 = px.bar(
        deaths_type,
        x="Disaster_Type",
        y="Deaths",
        title="Deaths by Disaster Type"
    )

    st.plotly_chart(fig1, use_container_width=True)

with col2:
    deaths_country = (
        filtered_df.groupby("Country")["Deaths"]
        .sum()
        .reset_index()
        .sort_values(by="Deaths", ascending=False)
        .head(10)
    )

    fig2 = px.bar(
        deaths_country,
        x="Country",
        y="Deaths",
        title="Top 10 Countries by Death Toll"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ---------------- ECONOMIC LOSS ANALYSIS ----------------
col3, col4 = st.columns(2)

with col3:
    damage_type = (
        filtered_df.groupby("Disaster_Type")["Total_Damages_USD"]
        .sum()
        .reset_index()
        .sort_values(by="Total_Damages_USD", ascending=False)
    )

    fig3 = px.treemap(
        damage_type,
        path=["Disaster_Type"],
        values="Total_Damages_USD",
        title="Economic Loss by Disaster Type"
    )

    st.plotly_chart(fig3, use_container_width=True)

with col4:
    damage_country = (
        filtered_df.groupby("Country")["Total_Damages_USD"]
        .sum()
        .reset_index()
        .sort_values(by="Total_Damages_USD", ascending=False)
        .head(10)
    )

    fig4 = px.bar(
        damage_country,
        x="Country",
        y="Total_Damages_USD",
        title="Top 10 Countries by Economic Loss"
    )

    st.plotly_chart(fig4, use_container_width=True)

# ---------------- GLOBAL MAP ----------------
st.subheader("🌍 Global Disaster Distribution")

map_df = (
    filtered_df.groupby("Country")
    .size()
    .reset_index(name="Disaster Count")
)

fig5 = px.choropleth(
    map_df,
    locations="Country",
    locationmode="country names",
    color="Disaster Count",
    title="Global Disaster Map"
)

st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")

st.markdown("""
### 👨‍💻 Developed By

**Siva S**

- B.Tech Artificial Intelligence & Data Science
- Sri Shakthi Institute of Engineering and Technology
- Data Analytics Enthusiast
""")