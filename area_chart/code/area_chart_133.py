




import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Year': [2018, 2019, 2020, 2021, 2022, 2023],
        'Mathematics (Students)': [200, 220, 230, 250, 270, 290],
        'Science (Students)': [180, 200, 220, 240, 260, 280],
        'Literature (Students)': [300, 280, 310, 330, 350, 370],
        'Computer Science (Students)': [250, 260, 270, 290, 310, 330],
        'History (Students)': [150, 170, 180, 200, 220, 240],
        'Language (Students)': [180, 190, 200, 220, 240, 260]}

# Convert dictionary to pandas DataFrame
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12,8))

# Set background grid
plt.grid(color='lightgrey', linestyle='--', linewidth=0.5, alpha=0.5)

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Round up to nearest multiple of 10, 100 or 1000
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y-axis limits
ax.set_ylim(0, max_total_value)

# Set y-axis ticks and tick labels
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x-axis limits
ax.set_xlim(0, len(df.index) - 1)

# Set x-axis ticks and tick labels
ax.set_xticks(np.arange(0, len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])

# Set x-axis tick label rotation
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

# Set colors and transparency
colors = ['orange', 'green', 'blue', 'red', 'purple', 'yellow']
alpha = 0.8

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], df.iloc[:, 6],
             colors=colors, alpha=alpha, labels=['Mathematics', 'Science', 'Literature', 'Computer Science', 'History', 'Language'])

# Set legend
plt.legend(loc='upper left')

# Set title
plt.title('Student Enrollment Trends by Subject from 2018 to 2023')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-140159_47.png', bbox_inches='tight')

# Clear current image state
plt.clf()