
#Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Create a dictionary to represent the data
data = {'Year': ['2015', '2016', '2017', '2018', '2019'],
        'Crop Production (tons)': [5000, 5200, 5500, 5100, 4800],
        'Livestock (heads)': [2000, 2200, 2400, 2800, 2500],
        'Poultry (heads)': [3000, 3200, 3100, 3300, 3000],
        'Fish (heads)': [4000, 3800, 3600, 3700, 3900],
        'Dairy Production (liters)': [1000, 1200, 1300, 1500, 1400]}

#Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

#Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

#Calculate max total value and round up to nearest multiple of 1000
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max()/1000)*1000

#Set y-axis range and ticks
ax.set_ylim([0, max_total_value])
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

#Plot area chart
ax.stackplot(df['Year'], df.iloc[:, 1:].values.T, labels=df.iloc[:, 1:].columns, alpha=0.7)

#Set x-axis label and ticks
ax.set_xlabel('Year')
ax.set_xlim(0, len(df.index)-1)

#Set background grid lines
ax.grid(axis='y', alpha=0.5)

#Rotate x-axis labels and set rotation mode
ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')

#Set legend
ax.legend(loc='upper left')

#Set title
ax.set_title('Agriculture and Food Production by Year')

#Automatically resize image
fig.tight_layout()

#Save figure
fig.savefig('output/final/area_chart/png/20231228-145339_7.png', bbox_inches='tight')

#Clear current image state
plt.clf()