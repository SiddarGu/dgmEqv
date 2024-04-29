
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import seaborn as sns

# Process data using dict and pandas
data = {
    "Category": ["Psychology", "Sociology", "Economics", "History", "Geography"],
    "Category.1": [35, 25, 15, 10, 15],
    "Category.2": [30, 20, 20, 10, 20],
    "Category.3": [40, 15, 10, 10, 25],
    "Category.4": [20, 25, 30, 10, 15],
    "Category.5": [25, 20, 15, 20, 20],
    "Category.6": [30, 18, 18, 12, 22],
    "Category.7": [15, 25, 25, 15, 20],
    "Category.8": [22, 22, 18, 18, 20],
    "Category.9": [20, 25, 15, 20, 20]
}

df = pd.DataFrame(data)
df.set_index("Category", inplace=True)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Plot heatmap chart using ax.imshow()
im = ax.imshow(df, cmap="Blues", interpolation="nearest")

# Add tick labels
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df.index)

# Center ticks
ax.set_xticks(np.arange(len(df.columns)) - 0.5, minor=True)
ax.set_yticks(np.arange(len(df.index)) - 0.5, minor=True)
ax.tick_params(which="minor", length=0)

# Add colorbar
cbar = plt.colorbar(im)

# Add title
plt.title("Interdisciplinary Distribution in Social Sciences and Humanities")

# Automatically resize the image
plt.tight_layout()

# Save figure as png
plt.savefig("output/final/heatmap/png/20231228-134212_96.png", bbox_inches="tight")

# Clear current image state
plt.clf()