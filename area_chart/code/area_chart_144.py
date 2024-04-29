
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dictionary with data
data = {"Category": ["Marketing", "IT", "Finance", "Healthcare", "Retail", "Education", "Real Estate", "Hospitality", "Logistics"],
        "Revenue ($)": [100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000],
        "Expenses ($)": [75000, 90000, 125000, 150000, 175000, 200000, 225000, 250000, 275000],
        "Profit ($)": [25000, 60000, 75000, 100000, 125000, 150000, 175000, 200000, 225000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(12,8))

# Calculate max total value for y axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Round up max total value to nearest multiple of 10, 100, or 1000
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set x and y axis limits and ticks
plt.xlim(0, len(df.index) - 1)
plt.ylim(0, max_total_value)
plt.xticks(np.arange(len(df.index)), df["Category"])

# Set random colors and transparency
colors = np.random.rand(len(df.columns) - 1, 3)
alphas = np.random.uniform(0.5, 0.8, len(df.columns) - 1)

# Plot area chart
ax = plt.stackplot(df.index, df.iloc[:, 1:].values.T, colors=colors, alpha=alphas)

# Set background grid lines
plt.grid(color="grey", linestyle="--", linewidth=0.5, alpha=0.3)

# Set legend
plt.legend(ax, df.columns[1:], loc="upper left")

# Add title and labels
plt.title("Revenue, Expenses, and Profit Analysis by Industry")
plt.xlabel("Category")
plt.ylabel("Amount ($)")

# Automatically resize image and save
plt.tight_layout()
plt.savefig("output/final/area_chart/png/20231228-140159_60.png", bbox_inches="tight")

# Clear current image state
plt.clf()