import matplotlib.pyplot as plt
import matplotlib.colors as colors 
import matplotlib.cm as cmx
import numpy as np

data_input = "Art Form,Annual Revenue (Million $),Public Engagement (Score),Global Reach (Millions),Cultural Impact (Score)\n Painting,2000,85,50,85\n Literature,1500,90,70,90\n Music,3000,95,100,100\n Cinema,4000,90,150,95\n Sculpture,1000,80,30,80\n Dance,750,85,40,90\n Theater,2000,90,60,95"

data_list = [item.split(',') for item in data_input.split('\n')]  
data_labels = data_list[0][1:]
data = np.array([[float(i) for i in item[1:]] for item in data_list[1:]])
line_labels = [item[0]+str(data[i, 2]) for i, item in enumerate(data_list[1:])]

fig, ax = plt.subplots(figsize=(10, 10))

cNorm  = colors.Normalize(vmin=min(data[:, 3]) - 5, vmax=max(data[:, 3]))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap='YlOrRd')

bubble_sizes = np.interp(data[:,2], (data[:,2].min(), data[:,2].max()), (600, 5000))

for i in range(data.shape[0]):
    color_value = scalarMap.to_rgba(data[i, 3])
    ax.scatter(data[i, 0], data[i, 1], s=bubble_sizes[i], color=color_value, alpha=0.5, edgecolors="w", linewidth=2, label=None)
    ax.scatter([], [], s=20, label=line_labels[i], color=color_value)   

ax.legend(title=data_labels[2], loc='upper left')
ax.grid(True)

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

cbar = plt.colorbar(scalarMap, ax=ax)
cbar.set_label(data_labels[3])

plt.title('Cultural and Economic Impact of Different Art Forms')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/99_202312301731.png')
plt.clf()
