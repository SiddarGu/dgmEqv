
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data as a dictionary
data = {"Year": [2020, 2021, 2022, 2023, 2024],
        "Policy 1 ($)": [30000, 32000, 34000, 36000, 38000],
        "Policy 2 ($)": [25000, 27000, 29000, 31000, 33000],
        "Policy 3 ($)": [20000, 22000, 24000, 26000, 28000],
        "Policy 4 ($)": [15000, 16000, 17000, 18000, 19000],
        "Policy 5 ($)": [10000, 11000, 12000, 13000, 14000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate max total value and set y-limits and ticks
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot area chart
ax.stackplot(df["Year"], df["Policy 1 ($)"], df["Policy 2 ($)"], df["Policy 3 ($)"], df["Policy 4 ($)"], df["Policy 5 ($)"], labels=["Policy 1", "Policy 2", "Policy 3", "Policy 4", "Policy 5"], colors=["#4c72b0", "#55a868", "#c44e52", "#8172b3", "#ccb974"], alpha=0.8)

# Set x-limits and ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(range(len(df.index)))
ax.set_xticklabels(df["Year"])

# Set x and y labels
ax.set_xlabel("Year")
ax.set_ylabel("Funding Allocation ($)")

# Set title
ax.set_title("Government Policies and Funding Allocation")

# Add grid lines
ax.grid(linestyle="--")

# Set legend
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

# Automatically resize and save figure
fig.tight_layout()
fig.savefig("output/final/area_chart/png/20231226-130527_2.png", bbox_inches="tight")

# Clear current figure state
plt.clf()