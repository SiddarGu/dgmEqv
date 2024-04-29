


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Create dictionary from data
data = {"Country": ["United States", "China", "India", "Russia", "Brazil", "Canada", "Australia"],
        "CO2 Emissions (Tonnes per Capita)": [16, 8, 4, 12, 6, 15, 13],
        "Green Energy Usage (%)": [20, 15, 10, 5, 25, 30, 35],
        "Waste Recycling (%)": [45, 40, 30, 20, 50, 35, 40],
        "Water Consumption (Liters per Capita)": [300, 400, 200, 100, 500, 350, 375],
        "Forest Coverage (%)": [35, 20, 25, 50, 30, 40, 45],
        "Air Quality Index": [75, 150, 200, 100, 175, 80, 90]}

# Convert dictionary to dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 6))

# Create heatmap using seaborn
ax = sns.heatmap(df.drop("Country", axis=1), annot=True, cmap="YlGnBu", linewidths=0.5, cbar=False)

# Set x and y labels
ax.set_xlabel("Environmental Factors", fontsize=12)
ax.set_ylabel("Countries", fontsize=12)

# Set x and y tick labels
ax.set_xticklabels(df.drop("Country", axis=1).columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df["Country"], rotation=0, ha="center")

# Set title
plt.title("Environmental Impact of Countries", fontsize=14)

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig("output/final/heatmap/png/20231228-155147_22.png", bbox_inches='tight')

# Clear current image state
plt.clf()