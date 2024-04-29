

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary from data
data = {"Country": ["United States", "China", "Russia", "India", "Japan", "Germany"],
        "Coal Production (Million Short Tons)": [600, 4000, 500, 1000, 200, 100],
        "Natural Gas Production (Billion Cubic Feet)": [25, 180, 150, 50, 30, 10],
        "Crude Oil Production (Million Barrels)": [550, 2500, 200, 500, 100, 50],
        "Nuclear Energy Production (Billion Kilowatt-hours)": [800, 1000, 500, 600, 800, 500],
        "Renewable Energy Production (Billion Kilowatt-hours)": [900, 1200, 800, 600, 400, 300]}

# Create dataframe from dictionary
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 6))

# Create heatmap chart using seaborn
import seaborn as sns
ax = sns.heatmap(df.set_index('Country'), cmap="YlGnBu")

# Set ticks and tick labels for x and y axis
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

# Add title
plt.title('Energy Production by Country')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-162116_29.png', bbox_inches='tight')

# Clear current image state
plt.clf()