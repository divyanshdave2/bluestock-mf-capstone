import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

raw_path = BASE_DIR / "data" / "raw"
processed_path = BASE_DIR / "data" / "processed"

print(raw_path)
print(processed_path)

st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    layout="wide"
)

st.title("📊 Mutual Fund Analytics Dashboard")

# Load data
performance = pd.read_csv(
    processed_path/"clean_performance.csv"
)

# Show dataset
st.subheader("Performance Dataset")
st.dataframe(performance.head())

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Funds",
    len(performance)
)

col2.metric(
    "Average 3Y Return",
    round(performance['return_3yr_pct'].mean(),2)
)

col3.metric(
    "Average Sharpe Ratio",
    round(performance['sharpe_ratio'].mean(),2)
)

import matplotlib.pyplot as plt

top_funds = performance.sort_values(
    "return_3yr_pct",
    ascending=False
).head(10)

fig, ax = plt.subplots(figsize=(10,5))

ax.barh(
    top_funds["scheme_name"],
    top_funds["return_3yr_pct"]
)

ax.set_title("Top 10 Funds by 3-Year Return")

st.pyplot(fig)

risk = st.sidebar.selectbox(
    "Select Risk Grade",
    ["All"] + list(performance["risk_grade"].unique())
)

if risk != "All":
    performance = performance[
        performance["risk_grade"] == risk
    ]

st.sidebar.title("Filters")

selected_risk = st.sidebar.selectbox(
    "Risk Grade",
    ["All"] + list(performance["risk_grade"].dropna().unique())
)

if selected_risk != "All":
    performance = performance[
        performance["risk_grade"] == selected_risk
    ]

import matplotlib.pyplot as plt

st.subheader("🏆 Top 10 Funds by 3-Year Return")

top_returns = performance.sort_values(
    "return_3yr_pct",
    ascending=False
).head(10)

fig, ax = plt.subplots(figsize=(10,5))

ax.barh(
    top_returns["scheme_name"],
    top_returns["return_3yr_pct"]
)

ax.set_xlabel("Return %")
st.pyplot(fig)

st.subheader("📈 Top Funds by Sharpe Ratio")

top_sharpe = performance.sort_values(
    "sharpe_ratio",
    ascending=False
).head(10)

st.dataframe(
    top_sharpe[
        ["scheme_name","sharpe_ratio"]
    ]
)

st.subheader("⚖️ Risk vs Return")

fig, ax = plt.subplots(figsize=(8,6))

ax.scatter(
    performance["std_dev_ann_pct"],
    performance["return_3yr_pct"]
)

ax.set_xlabel("Risk (Std Dev)")
ax.set_ylabel("3Y Return")

st.pyplot(fig)

st.subheader("⚖️ Risk vs Return")

fig, ax = plt.subplots(figsize=(8,6))

ax.scatter(
    performance["std_dev_ann_pct"],
    performance["return_3yr_pct"]
)

ax.set_xlabel("Risk (Std Dev)")
ax.set_ylabel("3Y Return")

st.pyplot(fig)

st.subheader("📋 Fund Details")

st.dataframe(
    performance.sort_values(
        "return_3yr_pct",
        ascending=False
    ).head(10)
)

st.subheader("💰 AUM Distribution")

fig, ax = plt.subplots()

ax.hist(
    performance["aum_crore"],
    bins=20
)

st.pyplot(fig)

import seaborn as sns

st.subheader("🔥 Correlation Heatmap")

cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio"
]

fig, ax = plt.subplots(figsize=(8,6))

sns.heatmap(
    performance[cols].corr(),
    annot=True,
    ax=ax
)

st.pyplot(fig)
