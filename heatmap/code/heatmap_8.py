
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Create dictionary for data
data = {
    'Case Type': ['Contract Law', 'Criminal Law', 'Family Law', 'Corporate Law', 'Environmental Law', 'Immigration Law'],
    'United States': [35, 25, 20, 10, 5, 5],
    'Canada': [40, 20, 15, 10, 8, 7],
    'United Kingdom': [30, 30, 20, 10, 5, 5],
    'Australia': [25, 30, 20, 15, 5, 5]
}

# Convert dictionary to dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(12,8))

# Plot heatmap using sns.heatmap()
ax = sns.heatmap(df.iloc[:,1:], annot=True, fmt='g', cmap='Blues', cbar=False)

# Set x and y ticks and labels
ax.set_yticks(np.arange(len(df['Case Type'])) + 0.5)
ax.set_yticklabels(df['Case Type'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_xticks(np.arange(len(df.columns[1:])) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')

# Set ticks and ticklabels in the center of rows and columns
ax.tick_params(axis='both', which='both', length=0, pad=10)
ax.set_yticklabels(df['Case Type'], rotation=0, ha='center', wrap=True)
ax.set_xticklabels(df.columns[1:], rotation=0, ha='center', wrap=True)

# Set title
plt.title('Legal Cases by Country and Type')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231225-210514_27.png', bbox_inches='tight')

# Clear current image state
plt.clf()