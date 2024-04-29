

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data dictionary
data = {'Category': ['Civil Law', 'Criminal Law', 'Corporate Law', 'Family Law', 'Employment Law', 'Property Law', 'Immigration Law'],
        'Legal Cases Filed': [500, 400, 300, 200, 150, 100, 50],
        'Legal Cases Resolved': [400, 350, 250, 150, 100, 80, 40],
        'Legal Cases Pending': [100, 50, 50, 50, 50, 20, 10]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(12, 8))

# Set axes
ax = fig.add_subplot(111)

# Plot area chart
ax.stackplot(df['Category'], df['Legal Cases Filed'], df['Legal Cases Resolved'], df['Legal Cases Pending'], labels=['Legal Cases Filed', 'Legal Cases Resolved', 'Legal Cases Pending'], colors=['#A2D6F3', '#F3D0A2', '#A2F3A2'], alpha=0.8)

# Set x limit
ax.set_xlim(0, len(df.index) - 1)

# Set y limit
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_ylim(0, max_total_value)

# Set y ticks
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(color='grey', linestyle='dashed', alpha=0.5)

# Set legend
ax.legend(loc='upper right', fontsize=12)

# Set title
ax.set_title('Law and Legal Affairs Statistics', fontsize=16)

# Set x and y labels
ax.set_xlabel('Category', fontsize=14)
ax.set_ylabel('Number of Cases', fontsize=14)

# Set x and y ticks and tick labels
ax.set_xticks(np.arange(len(df['Category'])))
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231226-130527_12.png', bbox_inches='tight')

# Clear current image state
plt.clf()