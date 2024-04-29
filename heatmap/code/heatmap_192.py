
#Import modules
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Create data dictionary
data = {'Department': ['Finance', 'Marketing', 'Sales', 'IT', 'HR'],
        'Employee Satisfaction (%)': [85, 80, 75, 90, 95],
        'Employee Turnover (%)': [10, 15, 20, 5, 2],
        'Employee Performance (%)': [90, 85, 80, 95, 98],
        'Employee Engagement (%)': [75, 70, 65, 80, 85],
        'Training Hours (hours)': [40, 35, 30, 45, 50]}

#Convert data to pandas dataframe
df = pd.DataFrame(data)

#Set department as index
df = df.set_index('Department')

#Create heatmap chart
fig, ax = plt.subplots(figsize=(12, 8))
im = ax.imshow(df, cmap='Blues')

#Add ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index)

#Loop over data and add text annotations to cells
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j], ha='center', va='center', color='black')

#Add colorbar
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Value', rotation=-90, va='bottom')

#Add title
ax.set_title('Employee Metrics by Department')

#Resize and save figure
fig.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_53.png', bbox_inches='tight')

#Clear current image state
plt.clf()