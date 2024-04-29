
#import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

#Create a dictionary with the given data
data = {'Department': ['IT', 'Marketing', 'Finance', 'Education', 'Healthcare', 'Science', 'Business', 'Government', 'E-commerce', 'Gaming', 'Mobile', 'Retail', 'Telecommunications', 'Automotive'],
        'Recruitment': [50, 40, 60, 30, 60, 50, 40, 30, 60, 50, 40, 30, 50, 40],
        'Training': [40, 50, 40, 60, 50, 60, 50, 40, 30, 30, 60, 50, 40, 30],
        'Retention': [60, 30, 50, 50, 40, 30, 30, 50, 30, 60, 50, 40, 60, 60],
        'Compensation': [30, 20, 30, 40, 30, 40, 30, 50, 30, 40, 30, 30, 50, 50]}

#Convert the data to a dataframe
df = pd.DataFrame(data)

#Convert the first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

#Set the figure size
fig = plt.figure(figsize = (10, 6))

#Create a stacked area chart using ax.stackplot()
ax = plt.axes()
ax.stackplot(df.iloc[:,0], df.iloc[:,1], df.iloc[:,2], df.iloc[:,3], df.iloc[:,4], labels=['Recruitment', 'Training', 'Retention', 'Compensation'], colors=['#008fd5', '#fc4f30', '#e5ae37', '#6d904f'], alpha=0.8)

#Set the background grid lines
ax.grid(linestyle='-', linewidth='0.5', color='lightgrey')

#Set the x and y axis ticks and tick labels
#70% probability of setting ticks and tick labels
if random.random() < 0.7:
  ax.set_xlim(0, len(df.index) - 1)
  ax.set_xticks(np.arange(len(df.iloc[:,0])))
  ax.set_xticklabels(df.iloc[:,0])
  ax.set_ylim(0, np.ceil(df.iloc[:,1:].sum(axis=1).max() / 10) * 10)
  ax.set_yticks(np.linspace(0, df.iloc[:,1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
  ax.set_yticklabels(ax.get_yticks(), rotation=45, ha='right', rotation_mode='anchor')
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

#Set the legend's position and labels
ax.legend(loc='upper left')
ax.set_ylabel('Number of Employees')

#Set the title
ax.set_title('Human Resource Management by Department')

#Automatically resize the image
plt.tight_layout()

#Save the image
plt.savefig('output/final/area_chart/png/20231228-140159_51.png', bbox_inches='tight')

#Clear the current image state
plt.clf()