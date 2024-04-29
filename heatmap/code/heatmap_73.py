

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Import data and process into a dataframe
data = {'Sector': ['Technology', 'Healthcare', 'Finance', 'Energy'], 
        'Revenue (Billion USD)': [500, 300, 400, 200],
        'Profit (Billion USD)': [150, 100, 200, 50],
        'Assets (Billion USD)': [700, 600, 800, 400],
        'Market Capitalization (Billion USD)': [800, 500, 600, 300],
        'Debt (Billion USD)': [300, 200, 400, 100]
       }

df = pd.DataFrame(data)

# Set figure size and create axes object
plt.figure(figsize=(10,8))
ax = plt.gca()

# Plot heatmap using seaborn
sns.heatmap(df.iloc[:, 1:], annot=True, fmt='.0f', cmap='Blues', ax=ax)

# Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(5) + 0.5)
ax.set_yticks(np.arange(4) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Sector'], ha='right', rotation_mode='anchor')

# Set title and labels
ax.set_title('Financial Performance by Sector')
ax.set_xlabel('Financial Data (Billion USD)')
ax.set_ylabel('Sector')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_64.png', bbox_inches='tight')

# Clear current image state
plt.clf()