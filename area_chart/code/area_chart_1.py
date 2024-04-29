

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
data = {"Year": [2019, 2020, 2021, 2022, 2023],
        "Education (%)": [35, 30, 25, 20, 15],
        "Healthcare (%)": [30, 35, 40, 45, 50],
        "Infrastructure (%)": [20, 20, 20, 20, 20],
        "Economy (%)": [15, 15, 15, 15, 15]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data with area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], labels=["Education", "Healthcare", "Infrastructure", "Economy"])

# Set x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(np.arange(0, len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0])
    ax.set_xlim(0, len(df.index) - 1)

    # Calculate max total value and set y axis ticks and ticklabels
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Add background grid lines
ax.grid(axis="y", linestyle=":")

# Set colors and transparency
colors = ["#5E9EA0", "#D2691E", "#FF8C00", "#228B22"]
alpha = 0.8

# Set legend and legend position
legend = ax.legend(loc="upper right")
legend.set_title("Unit")

# Set title
ax.set_title("Government Priorities and Spending Trends")

# Automatically resize image and save
plt.tight_layout()
plt.savefig("output/final/area_chart/png/20231226-103019_0.png", bbox_inches="tight")

# Clear current image state
plt.clf()