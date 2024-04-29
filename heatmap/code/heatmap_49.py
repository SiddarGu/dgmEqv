
# Python code
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data processing
data = {"Category": ["Sociology", "History", "Psychology", "Economics", "Political Science", "Anthropology", "Linguistics", "Philosophy", "Education"],
        "Number of Publications": [5000, 4500, 4000, 3500, 3000, 2500, 2000, 1500, 1000],
        "Number of Citations": [25000, 20000, 18000, 16000, 14000, 12000, 10000, 8000, 6000],
        "Number of Authors": [2000, 1500, 1300, 1200, 1000, 900, 800, 700, 500],
        "Number of References": [10000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000],
        "Number of Conferences": [400, 350, 300, 250, 200, 150, 100, 50, 25]}
df = pd.DataFrame(data)
df.set_index("Category", inplace=True)

# Set up figure and axes
fig, ax = plt.subplots(figsize=(12,10))

# Plot heatmap
heatmap = ax.imshow(df, cmap="Blues", interpolation="nearest")

# Add colorbar
if np.random.rand() < 0.4:
    fig.colorbar(heatmap)

# Set ticks and ticklabels
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df.index)

# Loop over data dimensions and create text annotations
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j],
                       ha="center", va="center", color="w")

# Add title and adjust layout
ax.set_title("Research Output in Social Sciences and Humanities")
fig.tight_layout()
fig.savefig("output/final/heatmap/png/20231228-124154_37.png", bbox_inches="tight")