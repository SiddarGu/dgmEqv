
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create dictionary for data
data = {"Category": ["USA", "Europe", "Asia", "South America", "Africa", "Oceania"],
        "Trucks (Units)": [500, 400, 600, 300, 200, 100],
        "Ships (Units)": [200, 300, 400, 200, 100, 50],
        "Planes (Units)": [300, 200, 500, 150, 50, 20],
        "Trains (Units)": [400, 350, 300, 250, 150, 80],
        "Vehicles (Units)": [600, 550, 700, 350, 250, 120]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Set background grid lines
ax.grid(color='lightgrey', linestyle='--')

# Calculate max total value for y axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Round up max total value to nearest multiple of 10, 100, or 1000
if max_total_value <= 10:
    max_total_value = 10
elif max_total_value > 10 and max_total_value <= 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value > 100 and max_total_value <= 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y axis limits and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot stacked area chart
ax.stackplot(df["Category"], df["Trucks (Units)"], df["Ships (Units)"], df["Planes (Units)"], df["Trains (Units)"], df["Vehicles (Units)"], labels=["Trucks", "Ships", "Planes", "Trains", "Vehicles"], colors=["#577590", "#E1B16A", "#1D4E89", "#F4D35E", "#284B63"], alpha=0.8)

# Set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5, borderpad=1, frameon=False)

# Set x axis tick labels
ax.set_xticklabels(df["Category"], rotation=45, ha='right')

# Set x axis limit
ax.set_xlim(0, len(df.index) - 1)

# Set x and y labels
ax.set_xlabel("Region")
ax.set_ylabel("Units")

# Set title
ax.set_title("Distribution of Transportation Units by Region")

# Automatically resize image
fig.tight_layout()

# Save image
fig.savefig("output/final/area_chart/png/20231228-131755_99.png", bbox_inches='tight')

# Clear current image state
plt.clf()