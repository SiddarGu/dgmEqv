

#Script
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Read in data from given text
data = {'Website': ['Facebook', 'Twitter', 'Instagram', 'LinkedIn'],
        'Unique Visitors (in Millions)': [100, 50, 75, 25],
        'Pageviews (in Millions)': [500, 250, 400, 150],
        'Bounce Rate (%)': [25, 30, 20, 35],
        'Time Spent (in Minutes)': [5, 3, 6, 4],
        'Likes (in Millions)': [50, 30, 40, 20],
        'Shares (in Millions)': [20, 15, 25, 10]}

#Convert data into pandas dataframe
df = pd.DataFrame(data)

#Set up figure and axes
fig, ax = plt.subplots(figsize=(10, 8))

#Create heatmap using seaborn
sns.heatmap(df.drop(['Website'], axis=1), annot=True, cmap='Blues', linewidths=0.5, square=True)

#Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(6)+0.5)
ax.set_yticks(np.arange(4)+0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticklabels(df['Website'], rotation=0, ha='right', rotation_mode='anchor', wrap=True)

#Add colorbar
cbar = ax.collections[0].colorbar
cbar.set_label('Metrics')

#Set title
plt.title('Social Media and Web Metrics')

#Automatically resize image and save figure
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_23.png', bbox_inches='tight')

#Clear current image state
plt.clf()