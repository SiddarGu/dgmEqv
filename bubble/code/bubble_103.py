import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.cm as cm

data = '''School,Admission Rate (%),Average GPA,Merit-based Scholarships (Number),Diversity Score
Harvard University,5,4.2,200,85
University of Cambridge,21,3.7,150,78
University of Tokyo,33,3.5,100,68
Stanford University,4,4.3,180,90
University of Oxford,17.5,3.8,170,80
Massachusetts Institute of Technology,7,4.2,220,82'''
data = [i.split(',') for i in data.split('\n')]
data_labels = data[0][1:]
data = np.array([i[1:] for i in data[1:]], dtype=float)
line_labels = [i[0] for i in data[1:]]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))
bubble_colors = data[:, 3]

norm = mcolors.Normalize(vmin=bubble_colors.min(), vmax=bubble_colors.max())
cmap = cm.get_cmap("viridis")

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=bubble_sizes[i], c=cmap(norm(bubble_colors[i])), label=None)
    ax.scatter([], [], c=cmap(norm(bubble_colors[i])), label=line_label)

sm = cm.ScalarMappable(norm=norm, cmap=cmap)
plt.colorbar(sm, label=data_labels[3])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.legend(title=data_labels[2], loc='upper left')

plt.title('Evaluation of Top Universities Admission Criteria and Diversity Score')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/276_202312310045.png', format='png')
plt.clf()
