
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define data
data = {'Field': ['Electrical Engineering', 'Mechanical Engineering', 'Chemical Engineering'],
        'Solar Energy': [65, 45, 35],
        'Wind Energy': [72, 30, 50],
        'Hydro Energy': [40, 55, 40],
        'Nuclear Energy': [20, 10, 20],
        'Fossil Fuels': [5, 5, 10],
        'Geothermal Energy': [10, 8, 3]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Set index to 'Field'
df.set_index('Field', inplace=True)

# Plot heatmap using seaborn
sns.set()
fig, ax = plt.subplots(figsize=(12,8))
sns.heatmap(df, annot=True, cmap='Blues', fmt='.0f', cbar=False)

# Set ticks and labels for x and y axis
ax.set_xticks(np.arange(len(df.columns))+0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(len(df.index))+0.5)
ax.set_yticklabels(df.index, rotation=0)

# Add title
plt.title('Renewable Energy Usage by Engineering Field')

# Automatically resize and save image
fig.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_50.png', bbox_inches='tight')