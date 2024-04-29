
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Create dictionary for data
data = {'Department': ['Sales', 'Marketing', 'IT', 'Finance', 'Human Resources'],
        'Turnover Rate (%)': [10, 12, 8, 15, 5],
        'Training Hours (hrs)': [30, 40, 50, 45, 35],
        'Promotion Rate (%)': [5, 6, 4, 8, 2],
        'Absenteeism Rate (%)': [2, 3, 1, 4, 1],
        'Salary Increase Rate (%)': [5, 6, 4, 8, 2],
        'Performance Rating (%)': [85, 90, 80, 95, 75]}

# Convert dictionary to dataframe
df = pd.DataFrame(data)

# Set the index to be the Department column
df.set_index('Department', inplace=True)

# Set figure size and create heatmap using seaborn.heatmap()
plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, cmap='Blues')

# Set x and y ticks to be in the center
plt.xticks(np.arange(0.5, len(df.columns)), df.columns, ha='right', rotation_mode='anchor', rotation=45)
plt.yticks(np.arange(0.5, len(df.index)), df.index, va='center')

# Add title and adjust layout
plt.title('Human Resources Metrics')
plt.tight_layout()

# Save figure and clear current state
plt.savefig('output/final/heatmap/png/20231228-131639_0.png', bbox_inches='tight')
plt.clf()