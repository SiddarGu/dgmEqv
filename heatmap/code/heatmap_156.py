
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
data = {'Genre': ['Renaissance', 'Baroque', 'Rococo', 'Romanticism', 'Impressionism'], 'Painting': [75, 60, 50, 30, 40], 'Sculpture': [15, 20, 30, 40, 30], 'Dance': [5, 10, 10, 10, 10], 'Theatre': [3, 5, 5, 10, 10], 'Music': [2, 5, 5, 10, 10]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10,8))

# Set x and y axis ticks and ticklabels
plt.xticks([0.5, 1.5, 2.5, 3.5, 4.5], ['Renaissance', 'Baroque', 'Rococo', 'Romanticism', 'Impressionism'], ha='right', rotation=45, rotation_mode='anchor')
plt.yticks([0.5, 1.5, 2.5, 3.5, 4.5], ['Painting', 'Sculpture', 'Dance', 'Theatre', 'Music'], rotation=0)

# Create heatmap with seaborn
import seaborn as sns
hm = sns.heatmap(df.set_index('Genre').T, cmap='Blues', annot=True, cbar=True)

# Set tick label position
hm.xaxis.tick_top()
hm.xaxis.set_label_position("top")
hm.tick_params(labeltop=True, labelbottom=False)

# Set title
plt.title('Artistic Styles in History')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_8.png', bbox_inches='tight')

# Clear current image state
plt.clf()