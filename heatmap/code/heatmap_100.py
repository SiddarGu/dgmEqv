
# import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# create dataframe from data
df = pd.DataFrame({'Platform': ['Instagram', 'Facebook', 'Twitter', 'YouTube', 'TikTok', 'Snapchat'], 
                   'Number of Users (Millions)': [1000, 1500, 800, 1200, 500, 300],
                   'Number of Posts (Millions)': [500, 750, 400, 600, 250, 150],
                   'Average Likes per Post': [200, 150, 100, 180, 90, 80],
                   'Average Comments per Post': [50, 45, 35, 60, 30, 25],
                   'Average Shares per Post': [30, 28, 25, 35, 20, 15]})

# set figure size
fig, ax = plt.subplots(figsize=(12,8))

# plot heatmap using sns.heatmap()
sns.heatmap(df.iloc[:,1:], annot=True, cmap='Blues', linewidths=.5, cbar=False)

# set x and y tick labels and rotate if necessary
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.Platform, rotation=0)

# set ticks to be in the center of each cell
ax.set_xticks(np.arange(0.5, len(df.columns)-1, 1))
ax.set_yticks(np.arange(0.5, len(df.Platform), 1))

# set title
plt.title('Social Media Engagement Metrics')

# automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-130949_1.png', bbox_inches='tight')

# clear current image state
plt.clf()
plt.close()