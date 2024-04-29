
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary of data
data = {
    'Category': ['High School', 'Undergraduate', 'Graduate', 'Post-Graduate', 'Doctoral'],
    'Mathematics (Students)': [200, 100, 150, 100, 200],
    'Computer Science (Students)': [150, 120, 180, 200, 180],
    'Engineering (Students)': [180, 150, 200, 250, 150],
    'Physics (Students)': [130, 100, 150, 180, 130],
    'Chemistry (Students)': [250, 200, 250, 150, 100]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(12, 8))

# Set axes
ax = fig.add_subplot(111)

# Calculate max total value for y axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)

# Plot area chart
ax.stackplot(df['Category'], df.iloc[:, 1:].values.T, labels=df.columns[1:])

# Set x and y axis limits and ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, max_total_value)
ax.set_yticks(yticks)

# Set x and y axis labels
ax.set_xlabel('Category')
ax.set_ylabel('Number of Students')

# Set title
ax.set_title('Student Enrollment in Science and Engineering Programs')

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Add grid lines
ax.grid(True, alpha=0.3)

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-155112_10.png', bbox_inches='tight')

# Clear current image state
plt.clf()
plt.close()