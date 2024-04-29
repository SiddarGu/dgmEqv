# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.cm import ScalarMappable
import seaborn as sns

# Read data
data="""Sport,Revenue (Billion $),Global Popularity (Score),Sponsorship Deals (Millions),Athlete Income (Million $)
Football,50,100,2000,75
Basketball,40,90,1500,65
Cricket,20,80,1000,50
Tennis,15,70,800,45
Golf,10,60,600,40
Baseball,9,50,500,35
Cycling,7,40,400,30
Rugby,6,30,300,25
Boxing,5,20,200,20"""
data = pd.DataFrame([x.split(',') for x in data.split('\n')])
data.columns = data.iloc[0]
data = data[1:]
data_labels = data.columns[1:].tolist()
line_labels = (data['Sport']+" "+data[data_labels[2]]).tolist()
data = np.array(data[data.columns[1:]], dtype='float')

# Normalize color and size
colors = (data[:, 3] - np.min(data[:, 3])) / (np.max(data[:, 3]) - np.min(data[:, 3]))
sizes = 600 + (data[:, 2] - np.min(data[:, 2])) / (np.max(data[:, 2]) - np.min(data[:, 2])) * 4400

fig, ax = plt.subplots(figsize=(12, 8))
cmap = plt.cm.viridis

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], color=cmap(colors[i]), s=sizes[i], alpha=0.6, edgecolors='w', label=None)
    ax.scatter([], [], c=cmap(colors[i]), alpha=0.6, s=20, label=line_label)

ax.legend(title=data_labels[2], loc="upper left")
plt.title('Global Revenue and Popularity of Different Sports and Their Impact on Athlete Income')
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
sm = ScalarMappable(cmap=cmap, norm=plt.Normalize(min(data[:,3]), max(data[:,3])))
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3])
plt.grid(True, which='both', color='grey', linewidth=0.5)
plt.tight_layout()  
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/263_202312310045.png')
plt.clf()
