
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Data processing
data = pd.DataFrame({'Cause': ['Education', 'Environment', 'Health', 'Poverty', 'Disaster Relief'], 'Donations (USD)': [5000000, 2500000, 4000000, 3000000, 2000000], 'Volunteers': [300, 200, 500, 400, 300], 'Beneficiaries': [500, 350, 600, 450, 300]})

# Plotting the chart
fig, ax = plt.subplots(figsize=(12,8))
heatmap = sns.heatmap(data[['Donations (USD)', 'Volunteers', 'Beneficiaries']].transpose(), annot=True, linewidths=0.5, cmap='Blues', square=True, cbar=True, ax=ax)

# Setting labels and ticks
ax.set_xticklabels(data['Cause'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(['Donations (USD)', 'Volunteers', 'Beneficiaries'], rotation=0, ha='center')
ax.set_xlabel('')
ax.set_ylabel('')

# Setting colorbar
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=12)
cbar.ax.set_ylabel('USD', rotation=90, size=12)

# Adding title
plt.title('Impact of Charity Organizations', size=14)

# Automatically resize image
plt.tight_layout()

# Save chart
plt.savefig('output/final/heatmap/png/20231228-155147_3.png', bbox_inches='tight')

# Clear current image state
plt.clf()