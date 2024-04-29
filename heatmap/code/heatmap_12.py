
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Create a dictionary from the given data
data = {"Country":["France", "Spain", "United States", "China", "Italy", "Turkey"],
        "Tourist Arrivals (Millions)":[89.5, 83.2, 79.6, 70.1, 65.3, 61.8],
        "Hotel Occupancy Rate (%)":[75, 80, 85, 70, 70, 65],
        "Average Daily Rate (USD)":[200, 150, 250, 120, 180, 100],
        "Revenue per Available Room (USD)":[75, 70, 100, 50, 65, 40],
        "Total Tourism Expenditure (USD)":[10000, 9000, 11000, 8000, 8500, 7000]
       }

# Create a pandas dataframe from the dictionary
df = pd.DataFrame(data)

# Set the country as the index
df = df.set_index("Country")

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 7))

# Plot the heatmap using seaborn
sns.heatmap(df, annot=True, cmap="YlGnBu", fmt=".0f", linewidths=.5, ax=ax)

# Set the title of the figure
ax.set_title("Tourism and Hospitality Metrics by Country")

# Set the ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(0.5, len(df.columns), 1))
ax.set_yticks(np.arange(0.5, len(df.index), 1))
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df.index, rotation=0, ha="right", rotation_mode="anchor")

# Align the ticks and ticklabels to be in the center of rows and columns
ax.tick_params(axis="x", pad=15, labeltop=True, labelbottom=False)
ax.tick_params(axis="y", pad=5, labelright=True, labelleft=False)

# Add a colorbar of the chart
cbar = ax.collections[0].colorbar
cbar.set_ticks([0, 20, 40, 60, 80, 100])
cbar.set_ticklabels(["0", "20", "40", "60", "80", "100"])
cbar.ax.tick_params(labelsize=10)

# Automatically resize the image
plt.tight_layout()

# Save the figure as a png file
plt.savefig("output/final/heatmap/png/20231225-210514_40.png", bbox_inches="tight")

# Clear the current image state
plt.clf()