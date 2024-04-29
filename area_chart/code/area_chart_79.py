
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a dictionary with the data
data = {"Production (Millions of Pounds)": [250, 300, 350, 400, 450, 500],
        "Corn (Bushels)": [200, 250, 300, 350, 400, 450],
        "Soybeans (Bushels)": [150, 200, 250, 300, 350, 400],
        "Wheat (Bushels)": [100, 150, 200, 250, 300, 350],
        "Rice (Pounds)": [0, 150, 200, 250, 300, 350]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data with the type of area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].T, labels=df.columns[1:])

# Set x and y axis ticks and ticklabels
if np.random.rand() > 0.3:
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha="right", rotation_mode="anchor")
if np.random.rand() > 0.3:
    # Calculate max total value
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    # Round up to the nearest multiple of 10, 100 or 1000
    if max_total_value < 1000:
        max_total_value = np.ceil(max_total_value / 10) * 10
    elif max_total_value < 10000:
        max_total_value = np.ceil(max_total_value / 100) * 100
    else:
        max_total_value = np.ceil(max_total_value / 1000) * 1000
    # Set y axis ticks and ticklabels
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
if np.random.rand() > 0.3:
    ax.set_ylabel("Production (Millions of Pounds)")

# Set background grid lines
ax.grid(color="grey", linestyle="dashed", linewidth=0.5)

# Set legend and adjust position
ax.legend(loc="upper left", bbox_to_anchor=(1.0, 1.0))

# Set title
fig.suptitle("Agricultural Production Trends by Crop", fontsize=16)

# Automatically resize the image
fig.tight_layout()

# Save the figure
fig.savefig("output/final/area_chart/png/20231228-131755_61.png", bbox_inches="tight")

# Clear the current image state
plt.clf()