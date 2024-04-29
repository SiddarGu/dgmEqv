

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data as a dictionary
data = {'Category': ['Breakfast', 'Lunch', 'Dinner', 'Snacks', 'Desserts'],
        'Coffee (Sales)': [800, 1000, 1200, 600, 400],
        'Tea (Sales)': [500, 600, 400, 300, 200],
        'Juice (Sales)': [400, 300, 500, 200, 100],
        'Soda (Sales)': [200, 400, 300, 400, 300],
        'Water (Sales)': [100, 100, 200, 100, 50]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and probability of setting ticks and ticklabels
fig, ax = plt.subplots(figsize=(10, 6))
prob = 0.7

# Plot the data with ax.stackplot()
ax.stackplot(df['Category'], df['Coffee (Sales)'], df['Tea (Sales)'], df['Juice (Sales)'], df['Soda (Sales)'], df['Water (Sales)'], labels=['Coffee', 'Tea', 'Juice', 'Soda', 'Water'])

# Set x and y axis ticks and ticklabels
if np.random.uniform(0, 1) <= prob:
    ax.set_xticks(np.arange(len(df['Category'])))
    ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
if np.random.uniform(0, 1) <= prob:
    ax.set_xlim(0, len(df.index) - 1)
if np.random.uniform(0, 1) <= prob:
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value/100) * 100
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11], dtype=np.int32)))
    ax.set_yticklabels(ax.get_yticks(), rotation=0, ha='right', rotation_mode='anchor')

# Set suitable colors and transparency
colors = ['#79c6e0', '#b3d7ff', '#80bfff', '#99ffe6', '#e5ffb3']
for i, patch in enumerate(ax.patches):
    patch.set_facecolor(colors[i%5])
    patch.set_alpha(0.7)

# Set background grid lines
ax.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.5)

# Set legend and adjust its position
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Automatically resize image
fig.tight_layout()

# Set title and labels
ax.set_title('Sales Distribution by Meal Type')
ax.set_xlabel('Category')
ax.set_ylabel('Sales')

# Save image
plt.savefig('output/final/area_chart/png/20231228-140159_67.png', bbox_inches='tight')

# Clear current image state
plt.clf()