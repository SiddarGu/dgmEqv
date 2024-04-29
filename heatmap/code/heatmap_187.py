
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# create a dictionary to store the data
data = {
    'Department': ['Sales', 'Marketing', 'IT', 'Finance', 'HR'],
    'Employee Satisfaction (%)': [80, 75, 90, 85, 95],
    'Salary ($)': [85000, 80000, 100000, 90000, 110000],
    'Health Benefits (%)': [95, 90, 98, 95, 100],
    'Vacation Days (#)': [15, 20, 10, 18, 10],
    'Training Hours (Hours)': [60, 50, 70, 65, 75],
    'Work-Life Balance (%)': [85, 80, 90, 85, 95]
}

# convert the dictionary to a dataframe
df = pd.DataFrame(data)

# set the Department column as the index
df.set_index('Department', inplace=True)

# plot the heatmap chart
fig, ax = plt.subplots(figsize=(10, 6)) # set the figure size
ax = sns.heatmap(df, annot=True, cmap='Blues') # use seaborn's heatmap function
ax.set_title('Employee Metrics by Department') # set the title of the chart
ax.set_xlabel('Metrics') # set the label for the x-axis
ax.set_ylabel('Department') # set the label for the y-axis

# rotate the x-axis tick labels and set them to the center of the columns
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')
plt.xticks(rotation=45, ha='left', rotation_mode='anchor')

# set the y-axis tick labels to the center of the rows
ax.yaxis.set_ticks_position('left')
ax.yaxis.set_label_position('left')

# resize the chart and save it
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_45.png', bbox_inches='tight')

plt.clf() # clear the current state of the image