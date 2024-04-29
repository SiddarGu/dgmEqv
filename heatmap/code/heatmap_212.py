
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define data
data = {
    "Category": ["Online Shopping", "Streaming Services", "Social Media", "Search Engines", "Cybersecurity"],
    "n North America": [70, 60, 80, 75, 85],
    "South America": [35, 45, 60, 55, 70],
    "Europe": [50, 55, 75, 65, 80],
    "Asia": [65, 50, 70, 60, 75],
    "Africa": [25, 30, 45, 40, 55],
    "Australia": [40, 45, 65, 50, 70]
}

# Convert data into dataframe
df = pd.DataFrame(data)
df = df.set_index("Category")

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot heatmap using sns.heatmap()
sns.heatmap(df, annot=True, cmap="Blues", fmt="g", linewidths=.5, cbar=True, annot_kws={"size": 12})

# Set axes ticks and labels
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.index)

# Set axes ticks in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns))+0.5, minor=False)
ax.set_yticks(np.arange(len(df.index))+0.5, minor=False)

# Set rotation and alignment for x-axis ticklabels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Set title
ax.set_title("Technology Adoption by Region", fontsize=18)

# Automatically resize image
fig.tight_layout()

# Save figure
plt.savefig("output/final/heatmap/png/20231228-134212_88.png", bbox_inches="tight")

# Clear current image state
plt.clf()