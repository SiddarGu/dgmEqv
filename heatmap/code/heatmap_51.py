
#Import required modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

#Create a dictionary with the data
data = {'Country':['China', 'United States', 'India', 'Russia', 'Japan', 'Germany', 'Canada', 'Brazil', 'Australia', 'South Africa'],
        'Electricity Production (TWh)':[7, 5.5, 4, 3, 2.5, 2, 1.5, 1, 0.8, 0.5],
        'Renewable Energy Production (TWh)':[1.5, 1.2, 0.8, 0.5, 0.7, 0.5, 0.4, 0.3, 0.2, 0.1],
        'Carbon Dioxide Emissions (MtCO2)':[10, 9, 7, 6, 5, 4, 3, 2, 1, 0.5],
        'Water Usage (billion m3)':[2.5, 2.2, 2.0, 1.5, 1.2, 1.0, 0.8, 0.5, 0.3, 0.2],
        'Waste Production (million tonnes)':[5, 4, 3, 2.5, 2, 1.5, 1, 0.8, 0.6, 0.4],
        'Forest Area (%)':[25, 20, 18, 15, 12, 10, 8, 6, 5, 4]}

#Convert the dictionary to a pandas dataframe
df = pd.DataFrame(data)

#Set the figure size
plt.figure(figsize=(12,8))

#Plot the heatmap chart using seaborn
sns.heatmap(df.iloc[:,1:], annot=True, cmap='BuPu', cbar=False, vmin=0, vmax=25)

#Set the title
plt.title('Environmental Impact by Country')

#Rotate the x-axis labels by 45 degrees and align them to the right
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

#Set the y-axis labels to the center of each row
plt.yticks(np.arange(10)+0.5, df['Country'], rotation=0)

#Automatically adjust the layout
plt.tight_layout()

#Save the chart as a png file
plt.savefig('output/final/heatmap/png/20231228-124154_39.png', bbox_inches='tight')

#Clear the current image state
plt.clf()