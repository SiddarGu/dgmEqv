import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import FuncFormatter

# Data transformation
data_raw = [
    ['Primary Education', 5000, 20, 40000, 95],
    ['Secondary Education', 3000, 15, 45000, 90],
    ['Higher Education', 2000, 10, 60000, 85],
    ['Technical Education', 1000, 8, 55000, 80],
    ['Special Education', 500, 5, 50000, 70],
    ['Continuing Education', 200, 4, 70000, 75]
]

data = np.array([row[1:] for row in data_raw])
line_labels = [f'{row[0]} ({row[3]})' for row in data_raw]
data_labels = ['Student Enrollment', 'Teacher-Student Ratio', 'Average Teacher Salary', 'Graduation Rate']

# Plotting
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot()

bubble_sizes = 600 + (data[:, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()) * 4400
color_map = colors.Normalize(data[:, 3].min(), data[:, 3].max())

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=bubble_sizes[i], c=data[i, 3], cmap='viridis', alpha=0.6, edgecolors='w', label=None, norm=color_map)
    ax.scatter([], [], c='k', alpha=0.3, s=20, label=line_label)
 
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.legend(title=data_labels[2])

color_bar = plt.colorbar(plt.cm.ScalarMappable(norm=color_map, cmap='viridis'), ax=ax)
color_bar.set_label(data_labels[3])

plt.title('Analysis of Education Data by Subject')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/376_202312311429.png')
plt.clf()
