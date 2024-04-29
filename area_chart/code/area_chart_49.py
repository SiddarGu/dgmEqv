
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary with data
data = {'Category': ['Physics (Projects)', 'Chemistry (Projects)', 'Biology (Projects)', 'Geology (Projects)', 'Environmental Science (Projects)'],
        '1': [20, 15, 25, 10, 30],
        '2': [15, 20, 30, 25, 10],
        '3': [25, 10, 20, 30, 15],
        '4': [10, 30, 15, 20, 25],
        '5': [30, 25, 10, 15, 20],
        '6': [20, 15, 25, 10, 30],
        '7': [15, 20, 30, 25, 10],
        '8': [25, 10, 20, 30, 15],
        '9': [10, 30, 15, 20, 25],
        '10': [30, 25, 10, 15, 20],
        '11': [20, 15, 25, 10, 30],
        '12': [15, 20, 30, 25, 10],
        '13': [25, 10, 20, 30, 15],
        '14': [10, 30, 15, 20, 25],
        '15': [30, 25, 10, 15, 20]}

# Convert dictionary to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(12, 8))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Ceil max total value up to the nearest multiple of 10, 100 or 1000
if max_total_value <= 10:
    max_total_value = 10
elif max_total_value <= 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value <= 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100

# Plot area chart with ax.stackplot()
ax = plt.axes()
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5],
             df.iloc[:, 6], df.iloc[:, 7], df.iloc[:, 8], df.iloc[:, 9], df.iloc[:, 10], df.iloc[:, 11],
             df.iloc[:, 12], df.iloc[:, 13], df.iloc[:, 14], 
             labels=['Physics', 'Chemistry', 'Biology', 'Geology', 'Environmental Science'], 
            #  colors=['#FFC107', '#4CAF50', '#2196F3', '#FF5722', '#9C27B0'], 
             alpha=0.8)
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, max_total_value)

# Set random background grid lines
ax.grid(color='#BDBDBD', linestyle='dotted', linewidth=1, alpha=0.3)

# Set x and y axis ticks with rotation and rotation_mode
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set legend and position
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1))

# Set title and labels
plt.title('Science and Engineering Project Distribution')
plt.xlabel('Category')
plt.ylabel('Projects')

# Automatically resize image
plt.tight_layout()

# Save figure as png
plt.savefig('output/final/area_chart/png/20231228-131755_24.png', bbox_inches='tight')

# Clear current image state
plt.clf()