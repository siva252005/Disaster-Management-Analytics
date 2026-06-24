import streamlit as st

st.set_page_config(
    page_title="Insights",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Key Insights & Recommendations")

st.markdown("---")

st.subheader("🌊 Most Frequent Disaster")
st.success("""
Floods are the most common disasters with more than 5,200 recorded events.
""")

st.subheader("⚡ Highest Economic Loss")
st.error("""
Storms caused the highest economic losses globally.
""")

st.subheader("☠️ Highest Death Toll")
st.warning("""
Earthquakes caused the largest number of deaths.
""")

st.subheader("🌏 Most Vulnerable Countries")
st.info("""
China, USA, India, Philippines, and Indonesia experience the highest number of disasters.
""")

st.subheader("📊 Decade Analysis")
st.success("""
The number of disasters increased significantly after the year 2000.
""")

st.subheader("🎯 Recommendations")

st.markdown("""
- Improve flood early warning systems.
- Strengthen earthquake-resistant infrastructure.
- Allocate more emergency resources to high-risk countries.
- Invest in disaster preparedness and public awareness.
- Use predictive analytics for future risk assessment.
""")