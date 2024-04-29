
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# transform data into array
data_labels = ['Employees (Thousands)', 'Salary (Average/Month)', 'Job Satisfaction (Score)', 'Benefits (Score)']
line_labels = ['Administrative','Technical','Financial','Managerial','Creative']
data = np.array([[50,3000,7,8],[40,4000,8,7],[30,5000,9,6],[20,6000,10,5],[10,7000,9,7]])

# create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# scaling of data
cmap = plt.cm.get_cmap('jet_r', 5)
norm = matplotlib.colors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
bubble_size = np.linspace(600, 5000, data[:,2].size)

# plot data
for i in range(data[:,2].size):
    ax.scatter(data[i, 0], data[i, 1], s=bubble_size[i], c=cmap(norm(data[i, 3])), label=None)
    ax.scatter([], [], s=20, c=cmap(norm(data[i, 3])), label=line_labels[i] + ' ' + str(data[i, 2]))

# plot legend
ax.legend(title=data_labels[2])

# plot color bar
smap = matplotlib.cm.ScalarMappable(cmap=cmap, norm=norm)
smap.set_array([])
fig.colorbar(smap, ax=ax, label=data_labels[3])

# other settings
ax.set_title("Employee Performance and Job Satisfaction in the Human Resources Industry")
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/35_2023122270050.png')
plt.clf()