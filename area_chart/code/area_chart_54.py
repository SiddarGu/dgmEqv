
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dictionary with the given data
data = {"Category": ["United States", "Europe", "Asia", "Africa", "South America"],
        "Baseball (Fans)": [40, 50, 30, 20, 40],
        "Soccer (Fans)": [50, 40, 20, 10, 30],
        "Basketball (Fans)": [30, 30, 40, 30, 20],
        "Hockey (Fans)": [20, 40, 20, 10, 30],
        "Football (Fans)": [60, 70, 50, 40, 50]}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Convert the first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate the max total value and round up to the nearest multiple of 10, 100, or 1000
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 10) * 10

# Set the y-axis limits and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot the area chart
ax.stackplot(df.index, df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=["#CDDC39", "#FF9800", "#3F51B5", "#673AB7", "#009688"], alpha=0.7)

# Set the x-axis limits and ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(df.index)
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha="right", rotation_mode="anchor")

# Set the grid lines
ax.grid(color="#BDBDBD", linestyle="--", linewidth=1, alpha=0.5)

# Set the legend and its position
ax.legend(loc="upper left")

# Set the title
ax.set_title("Global Distribution of Sports Fans by Region")

# Automatically resize the image and save it
plt.tight_layout()
plt.savefig("output/final/area_chart/png/20231228-131755_3.png", bbox_inches="tight")

# Clear the current figure
plt.clf()