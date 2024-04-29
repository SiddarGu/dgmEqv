
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Data processing
data = {'Genre': ['Renaissance', 'Baroque', 'Romanticism', 'Impressionism', 'Modernism'], 
        'Painting': [30, 25, 20, 15, 10], 
        'Sculpture': [20, 15, 10, 5, 5], 
        'Photography': [10, 5, 5, 5, 5], 
        'Music': [40, 50, 60, 70, 80], 
        'Dance': [30, 35, 40, 45, 50], 
        'Theatre': [20, 25, 30, 35, 40]}
df = pd.DataFrame(data, columns = ['Genre', 'Painting', 'Sculpture', 'Photography', 'Music', 'Dance', 'Theatre']) 
df = df.set_index('Genre')

# Plotting the heatmap
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df, annot=True, cmap='Blues', linewidths=.5, cbar=True, ax=ax)

# Setting ticks and ticklabels
ax.set_xticks(np.arange(len(df.columns)) + 0.5, minor=False)
ax.set_yticks(np.arange(len(df)) + 0.5, minor=False)
ax.set_xticklabels(df.columns, minor=False)
ax.set_yticklabels(df.index, minor=False)

# Rotating and wrapping the labels
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
plt.setp(ax.get_yticklabels(), wrap=True)

# Setting ticks and ticklabels in the center
ax.tick_params(axis='both', which='both', length=0, labelsize=12)
ax.tick_params(axis='x', which='major', pad=15)
ax.tick_params(axis='y', which='major', pad=15)

# Title and labels
plt.title('Artistic Preferences Throughout History', fontsize=15)
plt.xlabel('Art Forms', fontsize=12)
plt.ylabel('Genres', fontsize=12)

# Resizing and saving the figure
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_72.png', bbox_inches='tight')

# Clearing the plot
plt.clf()