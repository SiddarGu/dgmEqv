
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create data dictionary
data = {
    'Region': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia'],
    'Trucking': [2.5, 2.0, 3.0, 4.0, 1.5, 3.5],
    'Rail': [3.5, 2.8, 4.0, 5.5, 2.0, 4.5],
    'Air': [6.2, 5.5, 7.0, 9.5, 4.2, 8.0],
    'Maritime': [1.8, 1.5, 2.5, 3.5, 1.2, 2.8],
    'Pipeline': [2.0, 1.8, 2.5, 3.0, 1.5, 2.8]
}

# Convert data to dataframe
df = pd.DataFrame.from_dict(data)

# Set region as index
df.set_index('Region', inplace=True)

# Set figure size
plt.figure(figsize=(12,8))

# Plot heatmap using sns.heatmap()
sns.heatmap(df, annot=True, cmap='Blues')

# Set ticks and tick labels for x and y axis
plt.xticks(np.arange(5)+0.5, labels=df.columns, rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(6)+0.5, labels=df.index, rotation=0, ha='right', rotation_mode='anchor')

# Add title
plt.title('Freight Transport by Region')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231226-140552_9.png', bbox_inches='tight')

# Clear current image state
plt.clf()