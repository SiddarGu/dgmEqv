
# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define data
data = {'Location':['New York City','Paris','London','Tokyo','Rome'], 'Museums':[50,45,40,35,30], 'Theaters':[40,35,30,25,20], 'Galleries':[35,30,25,20,15], 'Festivals':[12,10,8,6,5], 'Art Schools':[8,6,4,3,2]}

# Create dataframe
df = pd.DataFrame(data)

# Set figure size
fig, ax = plt.subplots(figsize=(10,7))

# Plot heatmap chart
chart = sns.heatmap(df.set_index('Location'), annot=True, cmap='YlGnBu', linewidths=0.5, ax=ax)

# Set x and y axis ticks and tick labels
# ax.set_xticks(np.arange(len(df.columns)))
# ax.set_yticks(np.arange(len(df.index)))
# ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
# ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Set tick positions to the center of rows and columns
# ax.set_xticks(np.arange(len(df.columns))+0.5, minor=True)
# ax.set_yticks(np.arange(len(df.index))+0.5, minor=True)
# ax.tick_params(which='minor', length=0)

# Set title of figure
plt.title('Cultural Venues by Location')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231226-140552_5.png', bbox_inches='tight')

# Clear current image state
plt.clf()