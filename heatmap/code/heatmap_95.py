

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import data
data = {"Product Category": ["Soft Drinks", "Snacks", "Alcoholic Beverages", "Packaged Food", "Dairy Products"],
       "Revenue (in millions of dollars)": [2000, 3000, 1500, 2500, 1000],
       "Market Share (%)": [25, 30, 15, 20, 10],
       "Units Sold (in millions)": [1500, 2000, 1000, 1500, 500],
       "Average Price (in dollars)": [1.33, 1.50, 1.50, 1.67, 2.00],
       "Growth (%)": [5, 3, 2, 4, 1]}

# Convert to dataframe
df = pd.DataFrame(data)
df = df.set_index("Product Category") # Set index to Product Category

# Plot the heatmap chart
fig, ax = plt.subplots(figsize=(10,6))
heatmap = ax.imshow(df, cmap="Blues")

# Set x and y ticks and labels
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor", wrap=True)
ax.set_yticklabels(df.index, rotation=0, ha="right", rotation_mode="anchor", wrap=True)

# Loop over data dimensions and create text annotations
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j], ha="center", va="center", color="w")

# Set title and colorbar
ax.set_title("Revenue and Growth in the Food and Beverage Industry")
cbar = ax.figure.colorbar(heatmap)

# Automatically resize the image and save
fig.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-124154_94.png", bbox_inches="tight")

# Clear current image state
plt.clf()