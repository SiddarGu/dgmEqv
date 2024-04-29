
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Import data
data = {'Category': ['Traditional', 'Modern', 'Contemporary'],
        'Painting': [30, 50, 70],
        'Photography': [25, 55, 75],
        'Dance': [20, 45, 80],
        'Theatre': [35, 60, 85],
        'Sculpture': [40, 55, 90],
        'Music': [45, 50, 95]}

# Convert data to pandas dataframe
df = pd.DataFrame(data).set_index('Category')

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Plot heatmap using seaborn
sns.heatmap(df, annot=True, cmap='YlGnBu', ax=ax)

# Add colorbar
cbar = ax.collections[0].colorbar
cbar.set_ticks([20, 40, 60, 80, 100])
cbar.set_ticklabels(['20%', '40%', '60%', '80%', '100%'])

# Set x and y ticks and labels
plt.xticks(np.arange(6) + 0.5, labels=df.columns, ha='right', rotation_mode='anchor', rotation=45)
plt.yticks(np.arange(3) + 0.5, labels=df.index, va='center')

# Set title
plt.title('Art Forms and Styles by Category')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-124154_69.png', bbox_inches='tight')

# Clear current image state
plt.clf()