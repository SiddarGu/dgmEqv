
#Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Create dictionary with data
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Cancer': [500, 550, 600, 650, 700],
        'Heart Disease': [600, 650, 700, 750, 800],
        'Diabetes': [700, 750, 800, 850, 900],
        'Obesity': [800, 850, 900, 950, 1000],
        'Depression': [900, 950, 1000, 1050, 1100]}

#Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

#Set figure size
fig, ax = plt.subplots(figsize=(10,6))

#Plot area chart
ax.stackplot(df['Year'],df['Cancer'],df['Heart Disease'],df['Diabetes'],df['Obesity'],df['Depression'], labels=['Cancer','Heart Disease','Diabetes','Obesity','Depression'], colors=['#FFA07A','#FF7F50','#FFDAB9','#FFB6C1','#FF69B4'], alpha=0.7)

#Set legend position
ax.legend(loc='upper left')

#Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

#Set x and y axis ticks and ticklabels
if np.random.choice([0,1], p=[0.3,0.7]):
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df['Year'])))
    ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')
if np.random.choice([0,1], p=[0.3,0.7]):
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value % 1000 == 0:
        max_total_value = np.ceil(max_total_value / 1000) * 1000
    elif max_total_value % 100 == 0:
        max_total_value = np.ceil(max_total_value / 100) * 100
    elif max_total_value % 10 == 0:
        max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

#Set title
ax.set_title('Health Conditions by Year')

#Automatically resize image
fig.tight_layout()

#Save and show figure
plt.savefig('output/final/area_chart/png/20231228-131755_15.png', bbox_inches='tight')
plt.show()

#Clear current image state
plt.clf()