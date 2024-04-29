import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

data = '''Field,Number of Researchers (Thousands),Annual Funding (Billion $),Number of Patents Filed,Global Impact (Score)
 Computer Science,500,200,3000,8
 Civil Engineering,400,150,2500,7
 Mechanical Engineering,350,120,2000,6
 Chemical Engineering,300,100,1500,9
 Electrical Engineering,250,80,1000,8
 Aerospace Engineering,200,60,500,10
 Biomedical Engineering,150,40,250,7
 Environmental Engineering,100,20,100,9'''

rows = data.split('\n')
data_labels = rows[0].split(',')[1:]
line_labels = [row.split(',')[0] + " " + row.split(',')[2] for row in rows[1:]]
data = np.array([row.split(',')[1:] for row in rows[1:]], dtype=float)

cmap = plt.get_cmap("viridis")
norm = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())

fig, ax = plt.subplots(figsize = (12, 8))
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], c=cmap(norm(data[i, 3])), s=600 + 4400 * (data[i, 2]/data[:,2].max()), label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), s=20, label=line_label)
ax.legend(title=data_labels[2], loc='upper right')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

plt.colorbar(ScalarMappable(norm=norm, cmap=cmap), label=data_labels[3])
plt.title('Comparison of Various Fields in Science and Engineering')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/57_202312301731.png')
plt.clf()
