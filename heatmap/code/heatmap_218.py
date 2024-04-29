


# Sustainable Development Index by Country

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Process the data
data = {'Country':['United States', 'China', 'India', 'Japan', 'Germany'],
        'Renewable Energy (%)':[15, 20, 5, 10, 25],
        'Carbon Emissions (Tonnes per Capita)':[16, 10, 5, 12, 8],
        'Waste Diversion Rate (%)':[40, 50, 30, 60, 45],
        'Water Usage (Litres per Capita)':[300, 500, 200, 350, 400],
        'Forest Coverage (%)':[35, 21, 23, 43, 30],
        'Air Quality (AQI)':[50, 80, 100, 75, 60]}

df = pd.DataFrame(data).set_index('Country')

# Plot the chart
fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(df, ax=ax, annot=True, cbar=False, linewidths=0.5, cmap='Blues')

# Set ticks and ticklabels for x and y axis
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor', fontsize=10)
ax.set_yticklabels(df.index, fontsize=10)

# Set the ticks in the center of rows and columns
ax.set_xticks(np.arange(0.5, len(df.columns), 1))
ax.set_yticks(np.arange(0.5, len(df.index), 1))

# Set title and labels
ax.set_title('Sustainable Development Index by Country', fontsize=12)
ax.set_xlabel('Development Indicators', fontsize=10)
ax.set_ylabel('Country', fontsize=10)

# Automatically resize the image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_95.png', bbox_inches='tight')

# Clear the current image state
plt.clf()