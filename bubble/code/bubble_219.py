import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

# Given data
data = np.array([
    [250, 80000, 7, 10],
    [100, 70000, 8, 15],
    [300, 75000, 7, 12],
    [400, 85000, 6, 20],
    [200, 90000, 9, 8],
    [350, 77000, 8, 12],
    [500, 65000, 7, 22]
])
data_labels = ["Number of Employees", "Average Salary ($)", "Employee Satisfaction (Score)", "Annual Turnover Rate (%)"]
line_labels = ["Finance", "Human Resources", "Marketing", "Sales", "IT", "Operations", "Customer Service"]

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_title('Employee Management Metrics in Different Departments', fontsize=16)

# Normalize values for bubble size and color
size_normalizer = Normalize(data[:,2].min(), data[:,2].max())
color_normalizer = Normalize(data[:,3].min(), data[:,3].max())
cmap = cm.get_cmap('viridis')

for i, line_label in enumerate(line_labels):
    size = 600 + size_normalizer(data[i, 2]) * 4400
    color = cmap(color_normalizer(data[i, 3]))
    ax.scatter(data[i, 0], data[i, 1], c=[color], s=size, label=None, alpha=0.6, linewidths=2)
    ax.scatter([], [], c=color, alpha=0.6, s=20, label=line_label + f' {data[i, 2]}')

ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel(data_labels[1], fontsize=12)
ax.legend(title=data_labels[2], loc='upper left')

sm = plt.cm.ScalarMappable(cmap=cmap, norm=color_normalizer)
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3], rotation=-90, va="bottom")

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/315_202312310045.png', dpi=300)
plt.clf()
