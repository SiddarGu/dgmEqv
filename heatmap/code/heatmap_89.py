
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import seaborn to use sns heatmap
import seaborn as sns

# Set data
data = {"Production Line": ["Line A", "Line B", "Line C"],
        "Output (Units)": [100, 80, 75],
        "Defect Rate (%)": [2.5, 3.0, 3.5],
        "Downtime (Hours)": [1.5, 2.0, 2.5],
        "Cycle Time (Minutes)": [25, 30, 35],
        "Worker Efficiency (%)": [90, 85, 80],
        "Material Waste (%)": [1.5, 2.0, 2.5]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Set figure size
fig, ax = plt.subplots(figsize=(10,6))

# Plot heatmap using sns
sns.heatmap(df.iloc[:, 1:], annot=True, fmt=".2f", cmap="Blues", cbar=False)

# Set title
ax.set_title("Production Line Performance Metrics")

# Set x and y axis ticks and ticklabels to be in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns[1:])) + 0.5)
ax.set_yticks(np.arange(len(df["Production Line"])) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df["Production Line"])

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig("output/final/heatmap/png/20231228-124154_85.png", bbox_inches="tight")

# Clear the current image state
plt.clf()