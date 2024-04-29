import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# data
data_labels = ["Average Salary ($)", "Years of Experience", "Number of Publications", "Educational Attainment"]
line_labels = ["Biologist_10", "Chemist_12", "Physicist_15", "Engineer_14", "Mathematician_11", "Computer Scientist_17", "Geologist_13", "Astronomer_15", "Materials Scientist_12", "Environmental Scientist_10"]
data = np.array([[80000, 10, 50, 4],
                 [90000, 12, 60, 4],
                 [100000, 15, 70, 4],
                 [95000, 14, 65, 3],
                 [85000, 11, 55, 4],
                 [110000, 17, 80, 4],
                 [85000, 13, 60, 3],
                 [95000, 15, 75, 4],
                 [90000, 12, 65, 4],
                 [80000, 10, 55, 3]])

# normalize data for colormap
min_val = data[:, 3].min()
max_val = data[:, 3].max()
norm = mpl.colors.Normalize(vmin=min_val, vmax=max_val)
cmap = plt.cm.cool

fig, ax = plt.subplots(figsize=(14,10))
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], label=None,
               s=600 + 6000 * data[i, 2] / data[:, 2].max(), 
               c=cmap(norm(data[i, 3])), alpha = 0.6, edgecolors='w')
    ax.scatter([], [], label=line_labels[i],
               s=20, 
               c=cmap(norm(data[i, 3])), alpha = 0.6, edgecolors='w')

ax.legend(title=data_labels[2], loc="upper right")
ax.set_title('Salaries and Educational Attainment of Science and Engineering Professionals', fontsize=16)
ax.set_xlabel(data_labels[0], fontsize=14)
ax.set_ylabel(data_labels[1], fontsize=14)
ax.grid(True)

sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min_val, vmax=max_val))
sm.set_array([])
fig.colorbar(sm, label=data_labels[3])

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/330_202312311429.png')
plt.clf()
