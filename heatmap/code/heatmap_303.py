

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Process data
data = {"Category": ["North America", "South America", "Europe", "Asia", "Africa", "Australia"],
        "User Count (Millions)": [300, 200, 400, 500, 100, 50],
        "Internet Speed (Mbps)": [80, 60, 100, 120, 40, 80],
        "Number of Devices per Household": [5, 4, 6, 8, 2, 4],
        "Online Shopping Penetration (%)": [85, 70, 90, 95, 60, 70],
        "Social Media Usage (%)": [80, 65, 85, 90, 50, 75],
        "Online Gaming Penetration (%)": [60, 50, 70, 80, 40, 60]}
df = pd.DataFrame(data)
df.set_index("Category", inplace=True)

# Plot the data
fig, ax = plt.subplots(figsize=(12, 8))
heatmap = sns.heatmap(df, cmap="Blues", annot=True, fmt=".0f", cbar=False, ax=ax)

# Add labels and ticks
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df.index, rotation=0)
ax.set_xlabel("Internet and Technology Usage", fontsize=12)
ax.set_ylabel("Region", fontsize=12)
ax.tick_params(axis='both', which='both', length=0)

# Add colorbar
if np.random.choice([True, False], p=[0.4, 0.6]):
    cbar = heatmap.figure.colorbar(heatmap.collections[0])
    cbar.set_label("Percentage (%)", fontsize=12)

# Automatically resize and save the image
fig.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-163105_6.png", bbox_inches='tight')

# Clear the current image state
plt.clf()