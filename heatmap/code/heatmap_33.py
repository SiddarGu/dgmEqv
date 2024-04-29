
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Process the data
data = {"Region": ["North America", "South America", "Europe", "Asia", "Africa", "Australia"],
        "Wheat (Tonnes per Hectare)": [3.2, 2.8, 3.5, 4.0, 1.8, 3.1],
        "Corn (Tonnes per Hectare)": [5.5, 4.8, 5.2, 6.0, 2.5, 4.0],
        "Rice (Tonnes per Hectare)": [3.0, 3.2, 2.7, 6.5, 2.2, 3.6],
        "Soybeans (Tonnes per Hectare)": [2.5, 2.7, 2.2, 3.0, 1.5, 2.8],
        "Barley (Tonnes per Hectare)": [4.0, 3.5, 3.0, 5.5, 2.0, 4.2],
        "Potatoes (Tonnes per Hectare)": [6.1, 5.0, 4.8, 7.2, 3.5, 5.0]}

df = pd.DataFrame(data)
df = df.set_index("Region")

# Set the figure size
plt.figure(figsize=(10, 8))

# Plot the heatmap
ax = sns.heatmap(df, annot=True, cmap="YlGnBu", square=True)

# Set the ticks and ticklabels for x and y axis
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", fontsize=12)
ax.set_yticklabels(ax.get_yticklabels(), fontsize=12)

# Add title
plt.title("Crop Yields by Region in Agriculture", fontsize=18)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig("output/final/heatmap/png/20231228-124154_16.png", bbox_inches="tight")

# Clear the current image state
plt.clf()