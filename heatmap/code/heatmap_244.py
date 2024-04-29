


#Import modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#Create dictionary with data
data = {'Country':['United States', 'China', 'Russia', 'Germany', 'Brazil', 'India', 'Japan', 'Canada'],
        'Carbon Emissions (Million Metric Tons)':[500, 800, 350, 300, 400, 900, 200, 300],
        'Renewable Energy (%)':[10, 5, 15, 20, 10, 2, 15, 8],
        'Water Usage (Liters per Capita)':[5000, 4500, 3000, 3500, 4000, 3500, 4000, 3500],
        'Recycling Rate (%)':[30, 40, 25, 45, 35, 20, 50, 40],
        'Air Quality Index (AQI)':[50, 70, 60, 40, 65, 80, 35, 45]}

#Convert dictionary to dataframe
df = pd.DataFrame(data)

#Set figure size
plt.figure(figsize=(10,7))

#Plot heatmap using seaborn
sns.heatmap(df.set_index('Country'), annot=True, cmap='Blues', cbar=True)

#Set tick labels and format
plt.yticks(np.arange(0.5, len(df.index), 1), df['Country'], rotation=0, ha='right')
plt.xticks(np.arange(0.5, len(df.columns[1:]), 1), df.columns[1:], rotation=45, ha='right')

#Set title
plt.title('Environmental Impact by Country')

#Resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-155147_41.png', bbox_inches='tight')

#Clear current image state
plt.clf()