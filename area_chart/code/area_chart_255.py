
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Create a dictionary with the given data
data = {'Category': ['Fashion', 'Beauty', 'Travel', 'Food', 'Fitness', 'Entertainment', 'Technology', 'Lifestyle', 'Education', 'Health', 'News', 'Business', 'Sports'],
        'Facebook (Users)': [3000, 2000, 2500, 1800, 2000, 1500, 2000, 2500, 1500, 2000, 1800, 2500, 2000],
        'Twitter (Users)': [2000, 1500, 1800, 2000, 2500, 1000, 2500, 1800, 2000, 1500, 2500, 3000, 1500],
        'Instagram (Users)': [2500, 1800, 2000, 1500, 1800, 2500, 1500, 2000, 2500, 3000, 1000, 1500, 1800],
        'LinkedIn (Users)': [1500, 1000, 1500, 2500, 1500, 3000, 3000, 1000, 1800, 2500, 2000, 1800, 2500],
        'YouTube (Users)': [1000, 2500, 3000, 2000, 1000, 2000, 1800, 1500, 3000, 1800, 1500, 2000, 3000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Create a stacked area chart
ax.stackplot(df.index, df.iloc[:, 1:].values.T, labels=df.iloc[:, 0].values)

# Set the x-axis tick labels and tick positions
ax.set_xticklabels(df.iloc[:, 0].values)
ax.set_xticks(df.index)

# Set the x-axis limit
ax.set_xlim(0, len(df.index) - 1)

# Set the y-axis limit and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)
ax.set_ylim(0, max_total_value)

# Set the background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Set the legend
ax.legend(loc='upper left')

# Set the title
plt.title('Social Media and the Web User Distribution by Category')

# Automatically resize the image and save it
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-155112_13.png', bbox_inches='tight')

# Clear the current image state
plt.clf()