
#Import required modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Data processing
data = {'Region': ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia'],
        'Total Land (Hectares)': [1000000, 1500000, 2000000, 2500000, 3000000, 500000],
        'Crop Land (Hectares)': [500000, 750000, 1000000, 1250000, 1500000, 250000],
        'Forest Land (Hectares)': [300000, 400000, 500000, 600000, 800000, 100000],
        'Pasture Land (Hectares)': [150000, 200000, 250000, 300000, 400000, 50000],
        'Arable Land (Hectares)': [50000, 100000, 100000, 150000, 200000, 25000]}

df = pd.DataFrame(data).set_index('Region')

#Plotting the chart
fig, ax = plt.subplots(figsize=(12,8)) #Larger figsize setting to prevent content from being displayed

#Plot the chart using sns.heatmap()
sns.heatmap(df, annot=True, fmt='g', cmap='Blues', cbar=False) #Using the probability of 30% for sns.heatmap() 
#annot=True to show the value of each cell, fmt='g' to prevent scientific notation, cmap='Blues' for blue color scheme, cbar=False to not show colorbar

#Set x and y ticks and ticklabels
plt.yticks(np.arange(len(df.index))+0.5, df.index, rotation=0, ha='right', wrap=True) #Set y ticks and ticklabels with rotation=0 and wrap=True to prevent long labels from overlapping
plt.xticks(np.arange(len(df.columns))+0.5, df.columns, rotation=45, ha='right', wrap=True) #Set x ticks and ticklabels with rotation=45 and wrap=True to prevent long labels from overlapping

#Set ticks and ticklabels in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns))+0.5, minor=False)
ax.set_yticks(np.arange(len(df.index))+0.5, minor=False)

#Set title and labels
plt.title("Land Use by Region in Agriculture")
plt.xlabel("Land Type")
plt.ylabel("Region")

#Automatically resize the image
plt.tight_layout()

#Save the chart as a png file
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/heatmap/png_train/heatmap_202.png', bbox_inches='tight')

#Clear the current image state
plt.clf()

#Check the generated code to make sure it doesn't report errors, do not include undefined functions, and save path is relative path which is completely the same as output/final/heatmap/png.