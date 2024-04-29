
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


# Define data
data = {'Region': ['North America', 'Europe', 'Asia', 'Australia', 'Africa', 'South America'],
        'Truck (Kilometers)': [300, 150, 400, 200, 100, 250],
        'Rail (Kilometers)': [200, 300, 100, 50, 150, 100],
        'Air (Kilometers)': [400, 250, 150, 100, 50, 200],
        'Sea (Kilometers)': [100, 200, 300, 150, 200, 50],
        'Pipeline (Kilometers)': [50, 0, 500, 250, 100, 0]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 8))

# Create heatmap chart using sns.heatmap()
sns.heatmap(df.drop('Region', axis=1), cmap='Blues', annot=True, fmt='g')

# Set ticks and ticklabels for x and y axis
plt.xticks(np.arange(5)+0.5, df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(6)+0.5, df['Region'], rotation=0)

# Set title
plt.title('Transportation Usage by Region')

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig('output/final/heatmap/png/20231228-155147_15.png', bbox_inches='tight')

# Clear the current image state
plt.clf()