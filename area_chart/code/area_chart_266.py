
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data
data = {'Category': ['High School', 'Undergraduate', 'Graduate', 'Doctorate'],
        'Mathematics (Students)': [300, 400, 200, 100],
        'Science (Students)': [350, 450, 250, 150],
        'English (Students)': [250, 300, 150, 100],
        'History (Students)': [200, 250, 100, 50],
        'Foreign Language (Students)': [150, 200, 50, 20]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 6))

# Set colors and transparency
colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b2', '#ccb974']
alpha = 0.8

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Ceil max total value up to the nearest multiple of 10, 100 or 1000
if max_total_value <= 10:
    max_total_value = 10
else:
    max_total_value = np.ceil(max_total_value / 10) * 10

# Set y axis range and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x axis range
ax.set_xlim(0, len(df.index) - 1)

# Plot stacked area chart
ax.stackplot(df['Category'], df.iloc[:, 1:].T, colors=colors, alpha=alpha)

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Set x and y axis labels
ax.set_xlabel('Category')
ax.set_ylabel('Number of Students')

# Set legend
ax.legend(labels=df.columns[1:], loc='upper left')

# Set title
ax.set_title('Student Enrollment by Academic Level and Subject')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-155112_27.png', bbox_inches='tight')

# Clear current image state
plt.clf()