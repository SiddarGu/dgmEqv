
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create dictionary with data
data = {'Country': ['United States', 'China', 'India', 'Russia', 'Brazil'],
        'Greenhouse Gas Emissions (Tonnes per Capita)': [16, 10, 2, 25, 7],
        'Renewable Energy (%)': [12, 15, 8, 5, 20],
        'Forest Coverage (%)': [30, 22, 12, 40, 60],
        'Water Consumption (Liters per Capita)': [250, 200, 150, 300, 500]}

# Convert dictionary to pandas dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 8))

# Plot heatmap chart using seaborn
import seaborn as sns
ax = sns.heatmap(df.set_index('Country'), annot=True, fmt='.0f', cmap='BuPu')

# Set ticks and tick labels for x and y axis
ax.set_xticks(np.arange(0, 4) + 0.5, minor=False)
ax.set_yticks(np.arange(0, 5) + 0.5, minor=False)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Country'], rotation=0, ha='center')

# Add title
plt.title('Environmental Sustainability Measures by Country')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_63.png', bbox_inches='tight')

# Clear current image state
plt.clf()