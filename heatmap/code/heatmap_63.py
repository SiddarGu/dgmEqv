


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define data
data = {'Category': ['Retail', 'Finance', 'Technology', 'Healthcare', 'Food and Beverage'],
        'Revenue (Millions)': [500, 800, 1000, 1200, 600],
        'Profit (Millions)': [100, 200, 300, 400, 150],
        'ROI (%)': [20, 25, 30, 35, 22],
        'Debt to Equity': [1.5, 2.0, 2.5, 3.0, 2.2],
        'Market Share (%)': [30, 40, 60, 80, 45]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 6))

# Process data for heatmap
heatmap_data = df[['Revenue (Millions)', 'Profit (Millions)', 'ROI (%)', 'Debt to Equity', 'Market Share (%)']]
heatmap_data = heatmap_data.set_index(df['Category'])
heatmap_data = heatmap_data.transpose()

# Plot heatmap using seaborn
ax = sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, cbar_kws={'label': 'Value'})
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
# ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha='center')
ax.set_title('Business Performance Metrics')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-124154_51.png', bbox_inches='tight')

# Clear current image state
plt.clf()