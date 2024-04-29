

#Import modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Process data
data = {'Sport': ['Basketball', 'Football', 'Soccer', 'Tennis', 'Golf'],
        'Games Played': [82, 38, 38, 20, 20],
        'Goals Scored': [105, 55, 70, 30, 25],
        'Assists': [25, 30, 40, 10, 10],
        'Shots Taken': [150, 120, 130, 50, 40],
        'Fouls Committed': [75, 60, 70, 25, 20],
        'Passing Accuracy (%)': [87, 84, 88, 92, 95]}
df = pd.DataFrame(data)

#Set figure size and create plot
fig, ax = plt.subplots(figsize=(10,8))

#Plot heatmap
sns.heatmap(df.iloc[:,1:], annot=True, cmap='Blues', linewidths=0.5, cbar=False, ax=ax)

#Set x and y labels
ax.set_xlabel("Performance Metrics", fontsize=12)
ax.set_ylabel("Sport", fontsize=12)

#Set x and y ticks and ticklabels
ax.set_xticks(np.arange(len(df.columns)-1)+0.5)
ax.set_xticklabels(df.iloc[:,1:].columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(len(df))+0.5)
ax.set_yticklabels(df['Sport'], wrap=True)

#Set tick positions to center of cells
ax.tick_params(axis="x", length=0, pad=10)
ax.tick_params(axis="y", length=0, pad=10)

#Set title
ax.set_title("Performance Metrics by Sport")

#Resize image and save
fig.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-130949_14.png", bbox_inches='tight')

#Clear image
plt.clf()