
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {"Product": ["Product A", "Product B", "Product C"],
        "Production Line Efficiency (%)": [95, 92, 90],
        "Defective Products (%)": [3, 5, 7],
        "Downtime (Hours)": [2, 3, 4],
        "Waste (Tonnes)": [1.5, 2, 2.5],
        "Energy Consumption (kWh)": [20000, 24000, 28000]}

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Set ticks and tick labels for x and y axis
plt.yticks(range(len(df["Product"])), df["Product"], rotation=45, ha="right", rotation_mode="anchor")
plt.xticks(range(len(df.columns[1:])), df.columns[1:], wrap=True, rotation=45, ha="right", rotation_mode="anchor")

# Plot heatmap chart
im = ax.imshow(df.iloc[:, 1:].values, cmap="Reds")

# Add colorbar
cbar = plt.colorbar(im)

# Show value of each cell
for i in range(len(df)):
    for j in range(len(df.columns[1:])):
        text = ax.text(j, i, df.iloc[i, j + 1],
                       ha="center", va="center", color="w")

# Set title
plt.title("Production Metrics for Different Products")

# Automatically resize image
fig.tight_layout()

# Save figure
plt.savefig("output/final/heatmap/png/20231228-134212_49.png", bbox_inches="tight")

# Clear current image state
plt.clf()