from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

performance = pd.read_csv(
    BASE_DIR / "data" / "processed" / "clean_performance.csv"
)

def recommend_funds(risk_level):
    filtered = performance[
        performance["risk_grade"] == risk_level
    ]

    top3 = filtered.sort_values(
        by="sharpe_ratio",
        ascending=False
    ).head(3)

    return top3[
        ["scheme_name", "risk_grade", "sharpe_ratio"]
    ]

print(recommend_funds("High"))

# Kotak Emerging Equity Fund - Regular - Growth
# ICICI Pru Midcap Fund - Regular - Growth
# DSP Midcap Fund - Regular - Growth