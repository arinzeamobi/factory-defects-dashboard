# analysis_starter.py
# Quick-start analysis for 'Factory Defects & Yield Dashboard'
# Run with: python analysis_starter.py

import pandas as pd
import matplotlib.pyplot as plt

# 1) Load data
df = pd.read_csv("factory_defects_6mo.csv", parse_dates=["date"])

# 2) Basic checks
print("Rows:", len(df))
print(df.head())

# 3) KPI snapshots
daily = df.groupby("date").agg(
    total_defects=("defect_count","sum"),
    total_produced=("produced_count","sum"),
    downtime_min=("downtime_min","sum"),
    scrap_cost=("scrap_cost","sum")
).reset_index()
daily["yield_pct"] = (1 - daily["total_defects"] / daily["total_produced"]) * 100

print(daily.describe()[["total_defects","total_produced","yield_pct","scrap_cost"]])

# 4) Plot trend of yield
daily.plot(x="date", y="yield_pct", title="Daily Yield %")
plt.tight_layout()
plt.show()

# 5) Top defects overall
top_defects = df.groupby("defect_type")["defect_count"].sum().sort_values(ascending=False)
print("\nTop Defects:\n", top_defects)

# 6) Save a simple pivot to CSV (for Excel/Power BI)
pivot = df.pivot_table(index="defect_type", columns="line", values="defect_count", aggfunc="sum").fillna(0).astype(int)
pivot.to_csv("pivot_defects_by_line.csv")
print("\nSaved pivot_defects_by_line.csv")
