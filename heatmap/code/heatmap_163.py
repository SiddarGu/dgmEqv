
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data
data = {
    'Category': ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5', 'Category 6', 'Category 7', 'Category 8'],
    'Computer Technology': [50, 40, 30, 20, 10, 5, 2, 0],
    'Internet Speed': [75, 60, 50, 40, 30, 25, 20, 15],
    'Software': [80, 70, 60, 50, 40, 35, 30, 25],
    'Cloud Computing': [60, 50, 40, 30, 20, 15, 10, 5],
    'Mobile Devices': [90, 85, 80, 75, 70, 65, 60, 55]
}

# Convert data into pandas DataFrame
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 8))

# Set font size
sns.set(font_scale=1)

# Plot heatmap chart
ax = sns.heatmap(df.drop('Category', axis=1), annot=True, fmt='.0f', linewidths=.5, cmap="YlGnBu", cbar=True)

# Set tick labels and positions
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(len(df['Category'])) + 0.5)
ax.set_yticklabels(df['Category'], rotation=0)

# Set title
plt.title('Technology and Internet Adoption Rates')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_90.png', bbox_inches='tight')

# Clear figure
plt.clf()