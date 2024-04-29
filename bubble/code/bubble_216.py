import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import numpy as np

data_str = "Technology,Research Funding (Billion $),Number of Patents,Number of Graduates (Thousand),Innovation Score\n Software Engineering,40,1000,400,90\n Aerospace Engineering,35,800,310,88\n Biomedical Engineering,50,1200,280,92\n Civil Engineering,25,700,350,85\n Chemical Engineering,30,900,250,86\n Mechanical Engineering,20,650,300,83"
data_list = [i.split(',') for i in data_str.split('\n')]
data_labels = data_list[0][1:]
line_labels = [i[0] + " " + str(i[2]) for i in data_list[1:]]
data = np.array([list(map(float, i[1:])) for i in data_list[1:]])

fig, ax = plt.subplots(figsize=(12, 10))
cmap = plt.get_cmap("tab10")
c_norm = mcolors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
scalar_map = cm.ScalarMappable(norm=c_norm, cmap=cmap)

for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], c=scalar_map.to_rgba(data[i, 3]), s=((data[i, 2] - data[:,2].min())/(data[:,2].max() - data[:,2].min()))*4400 + 600, label=None)
    ax.scatter([], [], c=scalar_map.to_rgba(data[i, 3]), s=20, label=line_labels[i])
    
ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel(data_labels[1], fontsize=12)
ax.grid(True)

plt.colorbar(scalar_map, label=data_labels[3])

legend1 = ax.legend(loc='upper left', title=data_labels[2])
ax.add_artist(legend1)

plt.title('Examination of Research Funding, Patents, and Graduates in Different Engineering Fields', fontsize=15, y=1.05)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/170_202312310045.png')
plt.clf()
