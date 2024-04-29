


# import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# define data
data = [['Department', 'Employee Satisfaction (%)', 'Employee Turnover (%)', 'Training Hours', 'Productivity Index', 'Profit Margin (%)'],
        ['Sales', 85, 12, 40, 0.9, 25],
        ['Marketing', 80, 10, 30, 0.8, 22],
        ['Finance', 75, 8, 35, 0.7, 20],
        ['HR', 90, 5, 50, 0.95, 28],
        ['IT', 85, 7, 45, 0.85, 30],
        ['Operations', 80, 9, 40, 0.75, 22]]

# convert data to pandas dataframe
df = pd.DataFrame(data[1:], columns=data[0])

# set index as Department
df.set_index('Department', inplace=True)

# set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# plot heatmap using seaborn
sns.heatmap(df, annot=True, cmap='YlGnBu', annot_kws={'size': 12}, linewidths=0.5, ax=ax)

# set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(0.5, len(df.columns)))
ax.set_xticklabels(df.columns, rotation=45, rotation_mode='anchor', ha='right')
ax.set_yticks(np.arange(0.5, len(df.index)))
ax.set_yticklabels(df.index, rotation=0, rotation_mode='anchor', ha='right')

# set title
ax.set_title('Employee Performance Metrics by Department')

# adjust layout and save figure
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-155147_4.png', bbox_inches='tight')

# clear current image state
plt.clf()

# print success message
print('The heatmap chart has been successfully created and saved.')
