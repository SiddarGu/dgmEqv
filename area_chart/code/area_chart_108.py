
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create dictionary with data
data = {"Year": [2015, 2016, 2017, 2018],
        "Food Sales (millions)": [5000, 5200, 4500, 5100],
        "Beverage Sales (millions)": [4000, 4100, 4900, 3500],
        "Food Exports (millions)": [3000, 3200, 3000, 2800],
        "Beverage Exports (millions)": [2000, 2200, 2800, 2500]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set x and y ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(linestyle="dashed", color="gray")

# Plot data as stacked area chart
ax.stackplot(df["Year"], df.iloc[:, 1:].T, labels=df.columns[1:], alpha=0.8)

# Add legend
ax.legend(loc="upper left", fontsize=10)

# Set title and axis labels
ax.set_title("Sales and Exports in the Food and Beverage Industry from 2015 to 2018")
ax.set_xlabel("Year")
ax.set_ylabel("Sales and Exports (millions)")

# Automatically resize image and save
fig.tight_layout()
plt.savefig("output/final/area_chart/png/20231228-140159_14.png", bbox_inches="tight")

# Clear image state
plt.clf()