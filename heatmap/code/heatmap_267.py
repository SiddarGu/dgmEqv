
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data
data = {"Country": ["Thailand", "France", "Spain", "United States", "China", "Italy", "Australia", "Turkey"],
        "Tourist Arrivals (Millions)": [38.5, 39.8, 35.2, 70.5, 55.6, 29.4, 8.4, 41.7],
        "Tourist Receipts (Millions USD)": [50.2, 60.5, 45.6, 90.1, 75.8, 40.2, 10.6, 52.8],
        "Average Spending per Visitor (USD)": [1300, 1520, 1290, 1275, 1360, 1365, 1260, 1265],
        "Hotel Occupancy Rate (%)": [75.5, 80.5, 72.3, 85.2, 78.5, 70.5, 83.2, 76.1]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(12, 8))

# Plot heatmap chart using seaborn
sns.heatmap(df.iloc[:, 1:], annot=True, fmt=".0f", cmap="Blues", cbar=True)

# Set ticks and ticklabels for x and y axis
plt.xticks(np.arange(4) + 0.5, df.columns[1:], ha="right", rotation_mode="anchor", rotation=45)
plt.yticks(np.arange(8) + 0.5, df["Country"], rotation=0)

# Set ticks and ticklabels in the center of rows and columns
plt.tick_params(direction="inout", length=0.5, width=0.5)

# Set title
plt.title("Tourism and Hospitality Indicators by Country")

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig("output/final/heatmap/png/20231228-162116_22.png", bbox_inches="tight")

# Clear current image state
plt.clf()