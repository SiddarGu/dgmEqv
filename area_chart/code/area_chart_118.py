
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary for data
data = {"Category": ["Chinese", "Italian", "Mexican", "American", "Japanese", "Indian", "Thai", "French", "Fast Food", "Desserts"],
        "Restaurant Revenue ($)": [20000, 18000, 22000, 25000, 21000, 19000, 23000, 26000, 30000, 28000],
        "Grocery Sales ($)": [15000, 12000, 16000, 18000, 14000, 13000, 17000, 19000, 20000, 21000],
        "Alcohol Sales ($)": [5000, 4000, 6000, 7000, 5000, 6000, 7000, 8000, 10000, 9000],
        "Online Orders ($)": [3000, 2500, 3500, 4000, 3500, 3000, 4000, 4500, 5000, 4500],
        "Food Delivery Services ($)": [10000, 8000, 12000, 15000, 10000, 9000, 13000, 16000, 20000, 18000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12,8))

# Plot area chart
ax.stackplot(df.index, df.iloc[:, 1:].values.T, labels=df.iloc[:, 1:].columns, colors=["#FFC857", "#E9724C", "#C5283D", "#481D24", "#2E1F2A"], alpha=0.8)

# Set x and y axis ticks and ticklabels
if np.random.choice([0, 1], p=[0.3, 0.7]):
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(0, len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha="right", rotation_mode="anchor")
if np.random.choice([0, 1], p=[0.3, 0.7]):
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 100) * 100
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Adjust legend position
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

# Add grid lines
ax.grid(True, alpha=0.3)

# Set title
ax.set_title("Food Industry Analysis")

# Automatically resize image
fig.tight_layout()

# Save image
fig.savefig("output/final/area_chart/png/20231228-140159_29.png", bbox_inches="tight")

# Clear figure
plt.clf()