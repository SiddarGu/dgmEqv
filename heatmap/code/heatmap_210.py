
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Define data as a dictionary
data = {'Department': ['Sales', 'Marketing', 'Finance', 'Operations', 'Human Resources', 'IT'],
        'Employees': [50, 45, 40, 55, 35, 60],
        'Hiring Rate (%)': [10, 8, 9, 11, 7, 13],
        'Turnover Rate (%)': [15, 12, 13, 17, 10, 20],
        'Employee Satisfaction (%)': [80, 85, 75, 78, 90, 70],
        'Training Hours (hrs)': [50, 60, 55, 45, 40, 70],
        'Promotion Rate (%)': [20, 18, 15, 22, 12, 25]}

# Convert data into a pandas dataframe
df = pd.DataFrame(data)

# Set the index of the dataframe to 'Department'
df.set_index('Department', inplace=True)

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the heatmap using sns.heatmap()
sns.heatmap(df, annot=True, cmap='Blues', cbar_kws={'label': 'Scale'})

# Set the ticks and ticklabels for the x and y axis
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha='right', rotation_mode='anchor')

# Set the center of the rows and columns for the ticks
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)

# Set the ticklabels for the ticks
ax.set_xticklabels(df.columns, fontsize=12, ha='center')
ax.set_yticklabels(df.index, fontsize=12, va='center')

# Set the title of the figure
plt.title('Employee Performance and Satisfaction by Department', fontsize=14)

# Automatically resize the image
plt.tight_layout()

# Save the figure as a png image
plt.savefig('output/final/heatmap/png/20231228-134212_86.png', bbox_inches='tight')

# Clear the current image state
plt.clf()
plt.close()