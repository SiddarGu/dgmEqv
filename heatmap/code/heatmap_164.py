
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Process the data
data = {'Category': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia'],
        'Internet Speed (Mbps)': [35, 20, 50, 75, 10, 55],
        'Smartphone Penetration (%)': [75, 60, 80, 85, 30, 90],
        'Social Media Usage (hrs)': [3, 2, 4, 5, 1, 4],
        'E-commerce Sales (billion USD)': [800, 300, 1000, 1500, 100, 1200],
        'Online Banking Users (million)': [200, 100, 300, 500, 20, 400]}
df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

# Set the figure size
fig = plt.figure(figsize=(12, 8))

# Plot the heatmap chart
ax = sns.heatmap(df, annot=True, fmt='g', cmap='coolwarm')

# Set the ticks and ticklabels for x and y axis
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0)

# Set the ticks and ticklabels to be in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns)) + 0.5, minor=False)
ax.set_yticks(np.arange(len(df.index)) + 0.5, minor=False)

# Set the title of the figure
plt.title('Technology and Internet Usage by Region')

# Automatically resize the image
fig.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-131639_91.png', bbox_inches='tight')

# Clear the current image state
plt.clf()