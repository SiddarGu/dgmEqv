
data = {'Indicator': ['Education', 'Health', 'Employment', 'Income', 'Happiness'], 
        'United States': [75, 80, 70, 65, 75], 
        'Canada': [80, 85, 75, 70, 80], 
        'United Kingdom': [75, 80, 70, 65, 75], 
        'Germany': [80, 85, 75, 70, 80], 
        'France': [75, 80, 70, 65, 75], 
        'Japan': [80, 85, 75, 70, 80]}

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Convert data to dataframe
df = pd.DataFrame(data)
df.set_index('Indicator', inplace=True)

# Set figure size
fig = plt.figure(figsize=(10, 10))

# Plot heatmap using seaborn
sns.heatmap(df, annot=True, cmap='YlGnBu', center=np.mean(df), fmt='.0f')

# Set x and y ticks and ticklabels
plt.xticks(np.arange(len(df.columns)) + 0.5, df.columns, rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(len(df.index)) + 0.5, df.index, rotation=0, ha='right', rotation_mode='anchor')

# Add title
plt.title('Quality of Life Indicators by Country')

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/heatmap/png/20231228-134212_13.png', bbox_inches='tight')

# Clear current image state
plt.clf()