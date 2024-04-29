
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Define data as a dictionary
data = {'Category': ['Administration', 'Finance', 'Sales', 'Marketing', 'Engineering'], 
        'Employee Turnover Rate (%)': [10, 8, 12, 15, 5], 
        'Absenteeism Rate (%)': [2, 3, 5, 4, 1], 
        'Training Hours per Employee': [80, 75, 70, 85, 90], 
        'Employee Satisfaction (%)': [85, 82, 80, 88, 90], 
        'Salary Increase Rate (%)': [3, 2, 5, 4, 7]}

# Convert data into a pandas dataframe
df = pd.DataFrame(data)

# Set figure size
fig = plt.figure(figsize=(10, 8))

# Plot the heatmap chart
ax = sns.heatmap(df.iloc[:, 1:], annot=True, cmap='Blues', cbar=False)

# Set x and y axis ticks and ticklabels
ax.set_xticks(np.arange(5) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(5) + 0.5)
ax.set_yticklabels(df['Category'], rotation=0, wrap=True)

# Set ticks and ticklabels in the center of rows and columns
ax.tick_params(axis='both', which='both', length=0, pad=10)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Set title of the figure
plt.title('Employee Management Metrics')

# Save the image as png
plt.savefig('output/final/heatmap/png/20231228-131639_70.png', bbox_inches='tight')

# Clear the current image state
plt.clf()