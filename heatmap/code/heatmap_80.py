
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define data
data = {'Crop': ['Wheat', 'Rice', 'Corn'], 'North America': [3.2, 3.0, 5.5], 'South America': [2.8, 3.2, 4.8], 'Europe': [3.5, 2.7, 5.2], 'Asia': [4.0, 6.5, 6.0], 'Africa': [1.8, 2.2, 2.5], 'Australia': [3.1, 3.6, 4.0]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Set crop as index
df.set_index('Crop', inplace=True)

# Plot heatmap using seaborn
import seaborn as sns

# Set figure size
plt.figure(figsize=(12, 8))

# Set heatmap title
plt.title('Crop Yields by Region in Agriculture')

# Plot heatmap
sns.heatmap(df, annot=True, cmap='BuPu', linewidths=.5, cbar=False)

# Rotate x-tick labels
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

# Set x-tick labels in the center
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)

# Set y-tick labels in the center
plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=True)

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-124154_71.png', bbox_inches='tight')

# Clear current image state
plt.clf()