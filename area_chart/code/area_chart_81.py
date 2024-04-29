


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data as a dictionary
data = {
    'Department': ['Accounting', 'Customer Service', 'Legal', 'Operations', 'Procurement', 'Training & Development', 'Quality Assurance'], 
    'Administration (Employees)': [150, 200, 180, 120, 100, 150, 200], 
    'Sales (Employees)': [100, 180, 200, 150, 200, 180, 150], 
    'IT (Employees)': [120, 150, 150, 200, 180, 200, 100], 
    'HR (Employees)': [180, 120, 100, 170, 150, 130, 180], 
    'R&D (Employees)': [200, 100, 120, 130, 120, 100, 120]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)

# Calculate max total value and set y ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/10)*10

# Set y ticks
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(color='gray', linestyle='dashed', alpha=0.3)

# Plot the data as an area chart
ax.stackplot(df['Department'], df.iloc[:, 1:].values.T, labels=df.columns[1:], alpha=0.8)

# Set legend position and labels
ax.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0), title='Department', title_fontsize=12, fontsize=10)

# Set title and labels
ax.set_title('Employee Distribution by Department', fontsize=14)
ax.set_xlabel('Department', fontsize=12)
ax.set_ylabel('Number of Employees', fontsize=12)

# Automatically resize the image
plt.tight_layout()

# Save the chart as a png file
plt.savefig('output/final/area_chart/png/20231228-131755_64.png', bbox_inches='tight')

# Clear the current image state
plt.clf()