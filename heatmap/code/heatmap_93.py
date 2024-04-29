
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = {'Category': ['Criminal Law', 'Corporate Law', 'Intellectual Property Law', 'Immigration Law', 'Family Law', 'Employment Law', 'Environmental Law', 'Civil Rights Law'], 
        'Number of Lawyers': [500, 200, 100, 50, 300, 150, 50, 100], 
        'Average Salary ($)': [120, 200, 150, 100, 80, 120, 150, 100], 
        'Percentage of Female Lawyers (%)': [45, 35, 40, 55, 60, 50, 45, 60], 
        'Percentage of Minority Lawyers (%)': [30, 20, 25, 40, 50, 35, 20, 50], 
        'Number of Cases Filed': [300, 500, 200, 100, 400, 250, 150, 100]}

df = pd.DataFrame(data)
df = df.set_index('Category')

fig, ax = plt.subplots(figsize=(12, 8))

# Plot heatmap using sns
sns.heatmap(df, annot=True, cmap='Blues', fmt='g', cbar=False, ax=ax)

# Set ticks and ticklabels for x and y axis
plt.xticks(np.arange(len(df.columns))+0.5, df.columns, rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(len(df.index))+0.5, df.index, rotation=0)

# Add title and labels
plt.title('Diversity and Salary in Legal Fields')
ax.set_xlabel('Statistics')
ax.set_ylabel('Category')

# Automatically adjust subplot parameters to give specified padding.
plt.tight_layout()

# Save image
plt.savefig('output/final/heatmap/png/20231228-124154_91.png', bbox_inches='tight')

# Clear current image state
plt.clf()