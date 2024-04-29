
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# create dictionary from data
data = {
    'Job Title': ['Human Resources Manager', 'Employee Relations Specialist', 'Talent Acquisition Specialist', 'Compensation Analyst', 'Training and Development Manager'],
    'Number of Employees': [50, 30, 40, 25, 35],
    'Age Range': ['30-60', '25-45', '25-40', '25-55', '30-50'],
    'Gender Ratio (%)': [60, 40, 50, 55, 45],
    'Salary Range': [50, 45, 40, 55, 60],
    'Job Satisfaction (%)': [80, 75, 85, 70, 90]
}

# create dataframe from dictionary
df = pd.DataFrame(data)

# set figure size
fig, ax = plt.subplots(figsize=(10, 8))

# plot heatmap using seaborn
sns.heatmap(df[['Number of Employees', 'Gender Ratio (%)', 'Salary Range', 'Job Satisfaction (%)']].T, cmap='BuPu', annot=True, cbar=False, ax=ax)

# set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df['Job Title'])))
ax.set_yticks(np.arange(len(df.columns[1:5])))
ax.set_xticklabels(df['Job Title'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(['Employees', 'Gender Ratio', 'Salary Range', 'Job Satisfaction'])

# add title
plt.title('Employee Management Metrics')

# resize image
plt.tight_layout()

# save image
plt.savefig('output/final/heatmap/png/20231228-124154_53.png', bbox_inches='tight')

# clear current image state
plt.clf()