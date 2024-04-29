

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# import data
df = pd.DataFrame({'Category': ['Clothing', 'Electronics', 'Beauty', 'Home Goods', 'Food and Beverage'], 
                   'Retail Sales (in millions)': [50, 100, 75, 80, 150],
                   'Online Sales (in millions)': [25, 50, 35, 40, 75], 
                   'Market Share (%)': [12, 25, 18, 20, 37],
                   'Average Sales per Store (in thousands)': [250, 500, 300, 350, 700],
                   'Gross Profit Margin (%)': [45, 40, 50, 45, 35],
                   'Average Customer Rating (out of 5)': [4.5, 4.0, 4.2, 4.7, 4.8]})

# set figure size
fig, ax = plt.subplots(figsize=(10,8))

# create heatmap
sns.heatmap(df[['Retail Sales (in millions)', 'Online Sales (in millions)', 'Market Share (%)', 
                'Average Sales per Store (in thousands)', 'Gross Profit Margin (%)', 
                'Average Customer Rating (out of 5)']], cmap='YlGnBu', annot=True, fmt='.0f')

# set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(6) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(5) + 0.5)
ax.set_yticklabels(df['Category'], wrap=True, rotation=0)

# set labels and title
ax.set_xlabel('Performance Metrics')
ax.set_ylabel('Category')
ax.set_title('Retail and E-commerce Performance Metrics')

# resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-155147_11.png', bbox_inches='tight')

# clear current image state
plt.clf()