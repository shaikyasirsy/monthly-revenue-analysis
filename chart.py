# chart.py
# Email: 23f3000880@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -------------------
# Generate synthetic data
# -------------------
np.random.seed(42)
months = pd.date_range(start="2024-01-01", periods=12, freq='M')
segments = ["Regular", "Premium", "Wholesale"]

data = []
for seg in segments:
    base_revenue = np.random.randint(50000, 100000)
    seasonal_pattern = np.sin(np.linspace(0, 2 * np.pi, 12)) * 5000
    noise = np.random.normal(0, 3000, 12)
    revenue = base_revenue + seasonal_pattern + noise
    for m, r in zip(months, revenue):
        data.append({"Month": m, "Segment": seg, "Revenue": max(r, 0)})

df = pd.DataFrame(data)

# -------------------
# Seaborn Styling
# -------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# -------------------
# Create the lineplot
# -------------------
plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512px
sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    hue="Segment",
    marker="o",
    palette="deep"
)

plt.title("Monthly Revenue Trends by Customer Segment", fontsize=16, weight="bold")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)

# -------------------
# Save as 512x512 PNG
# -------------------
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches='tight')
plt.close()
