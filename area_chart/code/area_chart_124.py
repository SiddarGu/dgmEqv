
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create data dictionary
data = {"Category": ["North America", "South America", "Europe", "Asia", "Africa", "Oceania"],
        "Corn Production (tons)": [200000, 100000, 150000, 100000, 200000, 150000],
        "Wheat Production (tons)": [150000, 120000, 180000, 200000, 180000, 200000],
        "Soybean Production (tons)": [180000, 150000, 200000, 250000, 150000, 100000],
        "Rice Production (tons)": [130000, 100000, 150000, 180000, 130000, 250000],
        "Barley Production (tons)": [250000, 200000, 250000, 150000, 100000, 120000]
       }

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Set background grid lines
ax.grid(color="lightgrey", linestyle="--", linewidth=0.5)

# Set x and y axis ticks and ticklabels (70% probability)
ax.set_xlim(0, len(df.index) - 1)
if np.random.uniform() < 0.7:
    ax.set_xticks(np.arange(len(df)))
    ax.set_xticklabels(df.iloc[:, 0])
if np.random.uniform() < 0.7:
    # Calculate max total value and round up to nearest multiple of 10, 100, or 1000
    max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 10) * 10
    # Set yticks with random length from list of [3, 5, 7, 9, 11]
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(ax.get_yticks())

# Plot data as stacked area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5],
             labels=df.columns[1:6], alpha=0.6)

# Set legend and adjust position
ax.legend(loc="upper left", fontsize="small")
fig.tight_layout()

# Set title
ax.set_title("Crop Production by Region")

# Automatically resize image and save figure
fig.tight_layout()
fig.savefig("output/final/area_chart/png/20231228-140159_35.png", bbox_inches="tight")

# Clear current image state
plt.clf()