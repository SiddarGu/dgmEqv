
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load data into a dictionary
data = {'Category': ['Theater', 'Music', 'Visual Arts', 'Dance', 'Film/TV', 'Literature/n Classical', 'Modern', 'Contemporary', 'Pop', 'Jazz'],
        'Theater': [10, 20, 30, 20, 10, 10, 0, 0, 0, 0],
        'Music': [30, 20, 10, 20, 10, 10, 0, 0, 0, 0],
        'Visual Arts': [20, 30, 10, 10, 20, 10, 0, 0, 0, 0],
        'Dance': [10, 20, 10, 30, 20, 10, 0, 0, 0, 0],
        'Film/TV': [20, 10, 10, 20, 20, 20, 0, 0, 0, 0],
        'Literature/n Classical': [10, 20, 10, 30, 20, 10, 0, 0, 0, 0],
        'Modern': [0, 0, 0, 0, 0, 0, 30, 20, 10, 20],
        'Contemporary': [0, 0, 0, 0, 0, 0, 20, 30, 10, 10],
        'Pop': [0, 0, 0, 0, 0, 0, 10, 20, 10, 30],
        'Jazz': [0, 0, 0, 0, 0, 0, 20, 10, 10, 20]}

# Convert dictionary to pandas dataframe
df = pd.DataFrame(data)

# Set figure size
fig = plt.figure(figsize=(8,6))

# Set axes
ax = fig.add_subplot(111)

# Plot heatmap using seaborn
sns.heatmap(df.iloc[:, 1:], ax=ax, cmap='Blues', annot=True, fmt='g', cbar=False)

# Set x and y ticks and labels
ax.set_xticks(np.arange(len(df.columns)-1) + 0.5)
ax.set_yticks(np.arange(len(df)) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Category'], rotation=0, ha='right')

# Title
plt.title('Cultural Preferences by Category')

# Automatically resize image
fig.tight_layout()

# Save image
plt.savefig('output/final/heatmap/png/20231228-134212_55.png', bbox_inches='tight')

# Clear current image state
plt.clf()