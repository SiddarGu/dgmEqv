


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data
data = {
    'Technology': ['Artificial Intelligence', 'Internet of Things', 'Cloud Computing', 'Virtual Reality', 'Blockchain'],
    'Internet Usage (%)': [65, 50, 80, 40, 30],
    'Mobile Internet Usage (%)': [70, 55, 85, 45, 35],
    'E-commerce Penetration (%)': [50, 60, 90, 50, 40],
    'Social Media Users (%)': [45, 65, 95, 55, 45],
    'Online Gaming Revenue (%)': [35, 70, 100, 60, 50]
}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Set figsize for larger setting
plt.figure(figsize=(10, 8))

# Create heatmap chart using seaborn
sns.heatmap(df.drop('Technology', axis=1), annot=True, cmap='Blues')

# Set ticks and ticklabels for x and y axis
plt.xticks(np.arange(5) + 0.5, labels=df.drop('Technology', axis=1).columns, rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(5) + 0.5, labels=df['Technology'], rotation=0, ha='right', rotation_mode='anchor')

# Add title
plt.title('Emerging Technologies and Online Usage')

# Automatically resize image by tight_layout()
plt.tight_layout()

# Save image as png
plt.savefig('output/final/heatmap/png/20231228-124154_70.png', bbox_inches='tight')

# Clear current image state
plt.clf()