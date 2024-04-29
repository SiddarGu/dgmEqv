
#Import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Define data dictionary
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 
        'Production (units)': [1000, 1200, 1500, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400], 
        'Inventory (units)': [800, 900, 1100, 1300, 1500, 1600, 1800, 2000, 2200, 2400, 2600, 2800], 
        'Sales (units)': [900, 1000, 1200, 1500, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200]}

#Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

#Plot the data with area chart
fig, ax = plt.subplots(figsize=(10, 6)) #Larger setting for figsize
ax.stackplot(df['Month'], df['Production (units)'], df['Inventory (units)'], df['Sales (units)'], labels=['Production', 'Inventory', 'Sales'], colors=['#FFA07A', '#ADD8E6', '#90EE90'], alpha=0.8) #Set suitable colors and transparency
ax.legend(loc='upper left', bbox_to_anchor=(1, 1)) #Adjust legend's position
ax.set_title('Production, Inventory, and Sales Trends') #Set title
ax.set_xlabel('Month') #Set x-axis label
ax.set_ylabel('Units') #Set y-axis label
ax.grid(color='lightgrey', linestyle='dotted') #Set random background grid lines
ax.set_xlim(0, len(df.index) - 1) #Set x-axis ticks and ticklabels
max_total_value = df.iloc[:, 1:].sum(axis=1).max() #Calculate max total value
max_total_value = np.ceil(max_total_value / 100) * 100 #Ceil max total value up to nearest multiple of 100
ax.set_ylim(0, max_total_value) #Set y-axis range
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)) #Set y-axis ticks and ticklabels

#Automatically resize image
fig.tight_layout() 
plt.savefig('output/final/area_chart/png/20231228-131755_22.png', bbox_inches='tight') #Save image with bbox_inches='tight'

#Clear current image state
plt.clf() 