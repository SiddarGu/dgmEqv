import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib import colors

# Transform given data
data_labels = ['Annual Sales (Billion $)', 
               'Market Share (%)', 
               'Consumer Satisfaction (Score)', 
               'Environmental Impact (Score)']

raw_data = ['Coffee,500,15,80,7', 
            'Tea,380,12,85,8', 
            'Beer,600,18,75,6', 
            'Wine,440,13,90,5', 
            'Whisky,280,8,70,4', 
            'Cider,200,6,65,8', 
            'Non-Alcoholic,1000,28,85,9']
            
data = np.zeros((len(raw_data), len(data_labels)))

line_labels = []
for i, row in enumerate(raw_data):
    values = row.split(',')
    line_labels.append(values[0] + ' ' + str(values[2]))
    data[i] = values[1:]

# Normalize color and size
c_norm = colors.Normalize(vmin=np.min(data[:,3]), 
                          vmax=np.max(data[:,3]))

s_norm = colors.Normalize(vmin=np.min(data[:,2]),
                          vmax=np.max(data[:,2]))

# Create variables for color map and size map
c_map = plt.cm.jet
s_map = plt.cm.jet

# Create figure
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(1,1,1)

# Plot data
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], 
               c=c_map(c_norm(data[i, 3])),
               s=600 + 4400*s_norm(data[i, 2]), 
               label=None)
    ax.scatter([], [], c=c_map(c_norm(data[i, 3])),
               label=line_labels[i])

ax.legend(title=data_labels[2])

# Create colorbar
sm = ScalarMappable(norm=c_norm, cmap=c_map)
fig.colorbar(sm, ax=ax).set_label(data_labels[-1])

plt.title("Analysis of Sales, Market Share, and Environmental Impact in the Food and Beverage Industry 2023")
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.grid()

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/72_202312301731.png')
plt.clf()
