

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define data
data = {'Region': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia'],
        'Roadway (km)': [500000, 400000, 600000, 800000, 300000, 200000],
        'Railway (km)': [75000, 50000, 100000, 150000, 25000, 30000],
        'Waterway (km)': [100000, 75000, 150000, 200000, 50000, 40000],
        'Airway (km)': [50000, 40000, 75000, 100000, 25000, 20000],
        'Pipeline (km)': [25000, 20000, 30000, 50000, 15000, 10000]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 6))

# Plot heatmap using seaborn
ax = sns.heatmap(df.iloc[:, 1:], cmap='Blues', annot=True, fmt='g', cbar=False)

# Set x and y ticks and tick labels
ax.set_xticks(np.arange(len(df.columns) - 1) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(len(df['Region'])) + 0.5)
ax.set_yticklabels(df['Region'], rotation=0, ha='right', rotation_mode='anchor')

# Add title
ax.set_title('Transportation Infrastructure by Region')

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/heatmap/png/20231228-131639_32.png', bbox_inches='tight')

# Clear current image state
plt.clf()