

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data
data = {"Category": ["Soft Drinks", "Soda", "Energy Drinks", "Juice", "Water", "Alcoholic Drinks"],
        "Region": ["North America", "South America", "Europe", "Asia", "Africa", "Australia"],
        "Soft Drinks": [25, 30, 20, 15, 18, 25],
        "Soda": [35, 25, 30, 20, 25, 25],
        "Energy Drinks": [20, 15, 10, 25, 20, 15],
        "Juice": [10, 12, 25, 10, 10, 10],
        "Water": [8, 10, 10, 20, 10, 15],
        "Alcoholic Drinks": [2, 8, 5, 10, 15, 10]}

# Create dataframe from data
df = pd.DataFrame(data)

# Set figure size and create subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Create heatmap using seaborn
sns.heatmap(df.iloc[:, 2:], annot=True, linewidths=0.5, cmap="Blues", ax=ax)

# Set x and y tick labels
ax.set_xticklabels(df.columns[2:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df["Region"], rotation=0, ha='right', rotation_mode='anchor')

# Set ticks and tick labels in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns[2:])) + 0.5)
ax.set_yticks(np.arange(len(df["Region"])) + 0.5)

# Set title
ax.set_title("Beverage Consumption by Category and Region")

# Automatically resize image and save
plt.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-155147_44.png", bbox_inches='tight')

# Clear current image state
plt.clf()