import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

data_labels = ['Number of Students (Thousands)', 'Percentage Male (%)', 'Percentage Female (%)', 'Graduation Rate (%)', 'Employment Rate (%)']
line_labels = ['Mathematics', 'Physics', 'Biology', 'Engineering', 'English', 'History', 'Computer Science']
raw_data = np.array([
    [120, 45, 55, 72, 80],
    [80, 65, 35, 76, 82],
    [130, 40, 60, 70, 78],
    [200, 70, 30, 75, 88],
    [110, 35, 65, 80, 75],
    [90, 50, 50, 85, 70],
    [150, 60, 40, 83, 90],
])

fig, ax = plt.subplots(figsize=(12, 10))
cmap = plt.get_cmap("viridis")
norm = Normalize(vmin=np.min(raw_data[:, 3]), vmax=np.max(raw_data[:, 3]))

for i, line_label in enumerate(line_labels):
    size = (raw_data[i, 1]-np.min(raw_data[:, 1]))/(np.max(raw_data[:, 1])-np.min(raw_data[:, 1])) * 4400 + 600
    ax.scatter(raw_data[i, 0], raw_data[i, 2], c=cmap(norm(raw_data[i, 3])), s=size, label=None)
    ax.scatter([], [], c=cmap(norm(raw_data[i, 3])), s=20, label=f"{line_label}")

ax.legend(title=data_labels[2], loc='upper right')
plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax).set_label(label=data_labels[3])
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Comparative Analysis of Student Data in Different Subjects for 2023 in Higher Education')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/302_202312310045.png')
plt.clf()
