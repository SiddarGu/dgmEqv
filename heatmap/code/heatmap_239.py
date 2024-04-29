


# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data
data = {'Category': ['Search Engines', 'Social Media Platforms', 'E-commerce', 'Messaging Apps'],
        'Number of Websites': [3, 5, 4, 2],
        'Number of Users (in millions)': [500, 800, 300, 400],
        'Internet Speed (Mbps)': [200, 150, 100, 75],
        'Smartphone Penetration (%)': [65, 80, 50, 60],
        'Social Media Usage (Hours)': [10, 15, 8, 12]}

# Convert data into dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 8))

# Set font size
sns.set(font_scale=1.2)

# Plot heatmap chart using sns.heatmap()
sns.heatmap(df.iloc[:, 1:], annot=True, cmap='YlGnBu', cbar=False)

# Set ticks and labels for x-axis
plt.xticks(np.arange(4) + 0.5, labels=df['Category'], rotation=45, ha='right', rotation_mode='anchor', wrap=True)

# Set ticks and labels for y-axis
plt.yticks(np.arange(4) + 0.5, labels=['Search Engines', 'Social Media Platforms', 'E-commerce', 'Messaging Apps'], rotation=0, ha='right', rotation_mode='anchor', wrap=True)

# Add title
plt.title('Internet Usage by Category')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-155147_31.png', bbox_inches='tight')

# Clear current image state
plt.clf()