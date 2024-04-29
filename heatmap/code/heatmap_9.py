
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Import data
data = {"Country": ["China", "India", "United States", "Brazil", "Russia"],
        "Total Land Area (sq. km)": [9.6, 3.2, 6.8, 8.5, 17],
        "Agricultural Land Area (sq. km)": [1.2, 0.8, 1.5, 2.0, 3.5],
        "Crop Production (tonnes)": [1.5, 0.7, 1.2, 0.8, 0.5],
        "Livestock Production (tonnes)": [0.1, 0.05, 0.2, 0.15, 0.1],
        "Fish Production (tonnes)": [0.01, 0.005, 0.012, 0.008, 0.018]}
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(12, 6))

# Process data
x_labels = ["Total Land Area (million sq. km)", "Agricultural Land Area (million sq. km)", 
            "Crop Production (billion tonnes)",
            "Livestock Production (billion tonnes)", "Fish Production (billion tonnes)"]
y_labels = ["China", "India", "United States", "Brazil", "Russia"]
values = df.iloc[:, 1:].values

# Plot heatmap
ax = sns.heatmap(values, cmap="YlGnBu", annot=True, fmt='.3f', linewidths=.5, cbar=False)

# Set ticks and tick labels
ax.set_xticks(np.arange(0.5, len(x_labels) + 0.5))
ax.set_xticklabels(x_labels, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticks(np.arange(0.5, len(y_labels) + 0.5))
ax.set_yticklabels(y_labels, rotation=0, ha="right", rotation_mode="anchor")

# Set title
plt.title("Agriculture and Food Production by Country")

# Automatically resize image and save
plt.tight_layout()
plt.savefig("output/final/heatmap/png/20231225-210514_31.png", bbox_inches='tight')

# Clear figure
plt.clf()