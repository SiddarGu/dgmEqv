
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dictionary of data
data = {
    'Category': ['Sociology', 'History', 'Psychology', 'Political Science', 'Literature'],
    '2019': [300, 250, 280, 200, 150],
    '2020': [330, 270, 300, 230, 160],
    '2021': [350, 290, 320, 250, 180],
    '2022': [360, 310, 330, 260, 200],
    '2023': [370, 320, 340, 270, 210]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figsize
fig, ax = plt.subplots(figsize=(10, 6))

# Set x and y axis ticks and ticklabels
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])
ax.set_xlim(0, len(df.index) - 1)

# Calculate max total value and set y axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=df.columns[1:], colors=['#F9DC5C', '#FD6B6B', '#83D6DE', '#448AFF', '#FFB9B9'], alpha=0.7)

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Set legend and position
legend = ax.legend(loc='upper left')
legend.get_frame().set_alpha(0.8)

# Add title and labels
ax.set_title('Publications by Social Sciences and Humanities Categories from 2019 to 2023')
ax.set_xlabel('Category')
ax.set_ylabel('Publications')

# Automatically resize image
fig.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-140159_66.png', bbox_inches='tight')

# Clear current image state
plt.clf()