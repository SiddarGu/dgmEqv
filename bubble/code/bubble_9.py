
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Transform the given data into three variables
data_labels = ['Tourists (Millions)','Average Spending ($)','Satisfaction (Score)','Air Connectivity (Score)']
data = np.array([[50,1000,9,8],[80,1200,8,7],[90,800,7,9],[95,1500,10,6],[60,900,6,7],[70,1100,5,8]])
line_labels = ['Caribbean','Europe','SE Asia','USA','Africa','South Pacific']

fig, ax = plt.subplots(figsize=(12, 8))
# Color mapping and normalization
cmap = cm.RdYlGn
norm = plt.Normalize(vmin=min(data[:,3]), vmax=max(data[:,3]))
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

for i in range(data.shape[0]):
    bubble_size = (data[i,2] - data[:,2].min()) / (data[:,2].max() - data[:,2].min()) * (1000 - 600) + 600
    bubble_color = cmap(norm(data[i,3]))
    ax.scatter(data[i,0], data[i,1], s=bubble_size, color=bubble_color, label=None)
    ax.scatter([], [], s=20, color=bubble_color, label=line_labels[i] + ' ' + str(data[i,2]))

ax.legend(title=data_labels[2], loc='upper left')
plt.colorbar(sm, ax=ax, label=data_labels[3])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('Tourism and Hospitality Performance in Popular Destinations')

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/3_2023122270050.png')
plt.close()