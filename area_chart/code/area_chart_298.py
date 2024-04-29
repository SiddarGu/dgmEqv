
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary for data
data = {'Degree': ['Associate', 'Bachelor\'s', 'Master\'s', 'Doctorate', 'Professional', 'Total'],
        'Mathematics (Students)': [200, 100, 150, 100, 200, 750],
        'Education (Students)': [150, 120, 180, 200, 180, 830],
        'History (Students)': [180, 150, 200, 250, 150, 930],
        'Science (Students)': [130, 100, 150, 180, 130, 660],
        'Language (Students)': [250, 200, 250, 150, 100, 850]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(10,6))

# Set background grid lines
plt.grid(axis='y')

# Calculate max total value and set y limits and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
plt.ylim(0, max_total_value)
plt.yticks(yticks)

# Set colors and transparency
colors = ['skyblue', 'lightcoral', 'lightgreen', 'plum', 'gold']
alpha = 0.7

# Plot the chart using stackplot
ax = plt.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], colors=colors, alpha=alpha)

# Set x limits and ticks
plt.xlim(0, len(df.index) - 1)
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

# Set legend and its position
plt.legend(ax, ['Mathematics', 'Education', 'History', 'Science', 'Language'], loc='upper left')

# Set title
plt.title('Student Enrollment by Degree Type')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-161902_7.png', bbox_inches='tight')

# Clear current image state
plt.clf()