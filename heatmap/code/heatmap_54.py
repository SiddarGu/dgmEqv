
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
import seaborn as sns

# import data into a dictionary
data = {
    'Department': ['Marketing', 'Sales', 'Finance', 'HR', 'IT'],
    'Total Employees': [50, 60, 40, 30, 20],
    'Turnover Rate (%)': [12, 10, 8, 6, 4],
    'Average Salary ($)': [60000, 65000, 70000, 75000, 80000],
    'Employee Satisfaction (%)': [85, 80, 90, 95, 100],
    'Training Hours': [20, 25, 30, 35, 40]
}

# convert dictionary into a dataframe
df = pd.DataFrame(data)

# set x and y labels
x_label = 'Department'
y_label = ['Total Employees', 'Turnover Rate (%)', 'Average Salary ($)', 'Employee Satisfaction (%)', 'Training Hours']

# create a pivot table to organize data for heatmap
# pivot = df.pivot_table(index=y_label, columns=x_label, values='Employee Satisfaction (%)')

# plot the heatmap using seaborn
sns.heatmap(df.set_index('Department'), annot=True, cmap='Blues')

# set ticks and tick labels for x and y axis
plt.yticks(np.arange(len(df[x_label])) + 0.5, df[x_label], rotation=45, ha='right', rotation_mode='anchor')
plt.xticks(np.arange(5)+0.5, df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
# plt.yticks(np.arange(len(df[y_label].unique())) + 0.5, df[y_label].unique(), rotation=0, ha='right', rotation_mode='anchor')

# set title for the figure
plt.title('Employee Performance and Satisfaction by Department')

# resize the image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_41.png', bbox_inches='tight')

# clear current image state
plt.clf() 