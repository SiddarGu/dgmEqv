
# python code

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import data as dict
data = {'Department': ['Sales', 'Marketing', 'HR', 'IT'], 
        'Employee Turnover (%)': [5, 7, 3, 2], 
        'Salary ($)': [60000, 65000, 70000, 80000], 
        'Training Cost ($)': [5000, 6000, 8000, 10000], 
        'Hiring Time (days)': [30, 35, 40, 45], 
        'Employee Satisfaction (%)': [85, 80, 90, 95], 
        'Training Hours': [40, 50, 60, 70]}

# convert data to dataframe
df = pd.DataFrame(data)

# set figure size
plt.figure(figsize=(10, 8))

# plot heatmap using sns
import seaborn as sns
sns.heatmap(df.drop('Department', axis=1), annot=True, cmap='Blues')

# set x and y ticks
plt.xticks(np.arange(6), ('Employee Turnover (%)', 'Salary ($)', 'Training Cost ($)', 'Hiring Time (days)', 'Employee Satisfaction (%)', 'Training Hours'))
plt.yticks(np.arange(4), ('Sales', 'Marketing', 'HR', 'IT'))

# set ticks and ticklabels in the center of rows and columns
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=True)

# set x and y axis label
plt.xlabel('')
plt.ylabel('')

# add title
plt.title('Employee Management Metrics by Department')

# automatically resize the image
plt.tight_layout()

# save figure
plt.savefig('output/final/heatmap/png/20231228-163105_31.png', bbox_inches='tight')

# clear current image state
plt.clf()