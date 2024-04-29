
#import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#process data using pandas and dict
data = {'Year': ['2016', '2017', '2018', '2019', '2020'],
        'Wheat (Tonnes per Hectare)': [3.0, 3.2, 3.5, 3.8, 4.0],
        'Corn (Tonnes per Hectare)': [4.0, 4.5, 4.8, 5.0, 5.5],
        'Rice (Tonnes per Hectare)': [2.5, 2.8, 3.0, 3.2, 3.5],
        'Soybeans (Tonnes per Hectare)': [3.5, 3.8, 4.0, 4.2, 4.5],
        'Barley (Tonnes per Hectare)': [2.8, 3.0, 3.2, 3.5, 3.8],
        'Potatoes (Tonnes per Hectare)': [3.5, 4.0, 4.5, 5.0, 5.5]}

df = pd.DataFrame(data, columns = ['Year', 'Wheat (Tonnes per Hectare)', 'Corn (Tonnes per Hectare)', 'Rice (Tonnes per Hectare)', 'Soybeans (Tonnes per Hectare)', 'Barley (Tonnes per Hectare)', 'Potatoes (Tonnes per Hectare)'])

#set figure size
plt.figure(figsize=(10, 8))

#plot heatmap using seaborn
sns.heatmap(df.iloc[:,1:], annot=True, cmap='Blues', cbar=True)

#set ticks and tick labels for x and y axis
plt.xticks(np.arange(6)+0.5, df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(5)+0.5, df['Year'], rotation=0)

#set title of the figure
plt.title("Crop Yields by Year in Agriculture")

#automatically resize the image
plt.tight_layout()

#save figure as png
plt.savefig('output/final/heatmap/png/20231228-163105_11.png', bbox_inches='tight')

#clear current image state
plt.clf()