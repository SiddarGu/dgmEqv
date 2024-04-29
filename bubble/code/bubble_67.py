import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

data = '''Initiatives,Annual Budget (Million $),Carbon Footprint (Metric Tons),Renewable Energy (%),Sustainability (Score)
Recycling Program,100,5000,15,8
Green Energy Projects,200,10000,30,9
Water Conservation,50,2000,10,7
Forest Conservation,150,8000,25,9'''

lines = data.split('\n')
data_labels = lines[0].split(',')
line_labels = [line.split(',')[0] + line.split(',')[2] for line in lines[1:]]

data = np.array([line.split(',')[1:] for line in lines[1:]], dtype=float)

fig, ax = plt.subplots(figsize=(12,8))
scatter = ax.scatter(data[:, 0], data[:, 1], 
                     c=data[:, 3], cmap='viridis',
                     s=600 + (data[:, 2] - np.min(data[:, 2])) * (5000-600) / (np.max(data[:, 2])-np.min(data[:, 2])), 
                     label=None, alpha=0.5, 
                     norm=mcolors.Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3])))

for i, line_label in enumerate(line_labels):
    ax.scatter([], [], c='k', alpha=0.3, s=20, label=line_label)

ax.legend(title=data_labels[2])
ax.grid(True)

plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

plt.title('Environmental Initiatives and Sustainability Scores')

cbar = plt.colorbar(scatter)
cbar.set_label(data_labels[3])

plt.tight_layout()

plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/386_202312311429.png")

plt.clf()
