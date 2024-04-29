

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data processing
data = {"Country": ["United States", "China", "Japan", "United Kingdom", "Germany", "India"],
        "Data Usage (GB)": [50, 40, 30, 20, 15, 10],
        "Internet Speed (Mbps)": [25, 50, 30, 35, 20, 15],
        "Online Shopping (%)": [60, 80, 50, 40, 30, 20],
        "Smartphone Adoption (%)": [75, 90, 60, 55, 40, 30],
        "Social Media Usage (%)": [80, 90, 70, 60, 50, 40]}

df = pd.DataFrame(data)
df = df.set_index("Country")

# Plotting the heatmap chart
fig, ax = plt.subplots(figsize=(10, 7))
heatmap = ax.imshow(df, cmap="YlGnBu")

# Setting x and y ticks and ticklabels
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.index)

# Rotating x-axis labels if necessary
if len(df.columns[0]) > 6:
    ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor")

# Wrapping y-axis labels if necessary
if len(df.index[0]) > 6:
    ax.set_yticklabels(df.index, wrap=True)

# Setting ticks at the center of rows and columns
ax.set_xticks(np.arange(len(df.columns) + 1) - 0.5, minor=True)
ax.set_yticks(np.arange(len(df.index) + 1) - 0.5, minor=True)
ax.grid(which="minor", color="w", linestyle="-", linewidth=2)

# Adding colorbar with 40% probability
if np.random.uniform() < 0.4:
    fig.colorbar(heatmap)

# Adding labels to each cell if colorbar is not added
else:
    for i in range(len(df.index)):
        for j in range(len(df.columns)):
            text = ax.text(j, i, df.iloc[i, j],
                           ha="center", va="center", color="k")

# Setting title and saving the figure
ax.set_title("Technology and Internet Usage by Country")
fig.tight_layout()
plt.savefig("output/final/heatmap/png/20231225-210514_45.png", bbox_inches="tight")
plt.close()