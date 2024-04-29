
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data
data = {'Organization': ['World Wildlife Fund', 'Red Cross', 'Save the Children', 'Salvation Army'], 
        'Total Revenue (in millions)': [500, 750, 400, 300], 
        'Program Expenses (%)': [85, 75, 90, 80], 
        'Fundraising Expenses (%)': [7, 10, 5, 10], 
        'Administrative Expenses (%)': [8, 15, 5, 10]}

# Create dataframe
df = pd.DataFrame(data)
df = df.set_index('Organization')

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot heatmap
sns.heatmap(df, annot=True, cmap='Blues', linewidths=0.5, cbar=False)

# Set ticks and ticklabels
ax.set_xticks(np.arange(0.5, len(df.columns), 1))
ax.set_yticks(np.arange(0.5, len(df.index), 1))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Set tick and ticklabel positions
ax.tick_params(axis='x', which='major', pad=10)
ax.tick_params(axis='y', which='major', pad=10)

# Set title
plt.title('Financial Overview of Nonprofit Organizations')

# Automatically resize and save figure
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_22.png', bbox_inches='tight')

# Clear figure
plt.clf()