
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Import data
data = {"Region": ["North America", "South America", "Europe", "Asia", "Africa", "Australia"],
        "Truck (Count)": [500, 200, 300, 1000, 100, 300],
        "Train (Count)": [250, 150, 400, 800, 50, 200],
        "Ship (Count)": [300, 100, 250, 500, 25, 100],
        "Plane (Count)": [400, 100, 200, 1200, 50, 150],
        "Pipeline (Count)": [200, 50, 150, 600, 20, 75]}

df = pd.DataFrame(data)

# Set figure size
fig = plt.figure(figsize=(10, 8))

# Create heatmap
heatmap = sns.heatmap(df.set_index("Region").T, cmap="Blues", annot=True, fmt="g", cbar=False)

# Set ticks and ticklabels
heatmap.set_xticks(np.arange(len(df["Region"])) + 0.5)
heatmap.set_xticklabels(df["Region"], rotation=45, ha="right", rotation_mode="anchor", wrap=True)
# heatmap.set_yticks(np.arange(len(df.columns)) + 0.5)
# heatmap.set_yticklabels(df.columns)

# Set title
plt.title("Transportation by Region")

# Resize image and save
plt.tight_layout()
plt.savefig("output/final/heatmap/png/20231225-210514_22.png", bbox_inches="tight")

# Clear figure state
plt.clf()