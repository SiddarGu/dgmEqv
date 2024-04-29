
# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create dictionary with data
data = {'Category': ['Primary School', 'Middle School', 'High School', 'Undergraduate', 'Graduate', 'PhD'],
        'Physics (Students)': [180, 200, 250, 180, 100, 250],
        'Biology (Students)': [200, 180, 200, 250, 180, 200],
        'Chemistry (Students)': [150, 150, 180, 200, 250, 180],
        'Mathematics (Students)': [120, 130, 150, 150, 200, 150],
        'Literature (Students)': [100, 100, 100, 120, 150, 120]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data as stacked area chart
ax.stackplot(df['Category'], df['Physics (Students)'], df['Biology (Students)'], df['Chemistry (Students)'],
             df['Mathematics (Students)'], df['Literature (Students)'], labels=df.columns[1:])

# Set ticks and ticklabels for x axis
ax.set_xticks(np.arange(len(df['Category'])))
ax.set_xticklabels(df['Category'])

# Set ticks and ticklabels for y axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set grid lines
ax.grid(which='major', axis='both', linestyle='--', alpha=0.5)

# Set legend
ax.legend(loc='upper left')

# Set title
ax.set_title('Student Enrollment in Different Academic Levels')

# Automatically resize image
fig.tight_layout()

# Save image
plt.savefig('output/final/area_chart/png/20231228-140159_46.png', bbox_inches='tight')

# Clear current image state
plt.clf()