


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Input data
data = {'Region': ['Global', 'North America', 'Europe', 'Asia', 'Africa', 'Australia'],
        'Internet Usage': [70, 75, 72, 68, 65, 70],
        'Cloud Computing Usage': [60, 65, 62, 58, 55, 60],
        'Social Media Usage': [50, 55, 52, 48, 45, 50],
        'Artificial Intelligence Usage': [40, 45, 42, 38, 35, 40],
        'Internet Security': [80, 85, 82, 78, 75, 80],
        'Online Shopping': [30, 25, 32, 28, 35, 30]
        }

# Convert data to dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 6), dpi=80)

# Set axis labels and title
plt.xlabel('Technology Usage', fontsize=12)
plt.ylabel('Region', fontsize=12)
plt.title('Technology Usage by Region', fontsize=14)

# Create heatmap plot
ax = plt.gca()
heatmap = ax.imshow(df.iloc[:, 1:], cmap='Blues')

# Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df['Region'])))
ax.set_xticklabels(df.columns[1:], fontsize=12, ha='right', rotation_mode='anchor', rotation=45)
ax.set_yticklabels(df['Region'], fontsize=12, ha='right', rotation_mode='anchor', rotation=0)

# Loop over data dimensions and create text annotations
for i in range(len(df['Region'])):
    for j in range(len(df.columns[1:])):
        text = ax.text(j, i, df.iloc[i, j + 1], ha='center', va='center', color='black')

# Add colorbar
cbar = plt.colorbar(heatmap, shrink=0.6, aspect=15)
cbar.set_label('Usage (%)', fontsize=12)

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231226-140552_19.png', dpi=80, bbox_inches='tight')

# Clear current image state
plt.clf()