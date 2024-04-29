import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from matplotlib.cm import ScalarMappable

# process the data
data = np.array([
    ['HR', 200, 75000, 80, 10],
    ['Sales', 500, 85000, 75, 12],
    ['Finance', 300, 90000, 85, 8],
    ['IT', 250, 95000, 82, 9],
    ['Marketing', 400, 80000, 78, 11],
    ['Operations', 600, 70000, 79, 13]
], dtype=object)
data_labels = ['Number of Employees', 'Average Salary ($)', 'Employee Satisfaction (Score)', 'Employee Turnover (%)']
line_labels = [f"{row[0]} {row[2]}" for row in data]

# plot the data
sizes = data[:,2].astype(int)
colors = data[:,3].astype(int)
norm = mcolors.Normalize(vmin=min(colors), vmax=max(colors))
bubble_sizes = np.interp(sizes, (sizes.min(), sizes.max()), (600, 5000))
fig, ax = plt.subplots(figsize=(10, 8))

scatter = ax.scatter(data[:, 1], data[:, 2], label=None, c=colors, cmap='viridis', norm=norm, alpha=0.6, edgecolors='w', s=bubble_sizes)
for i, line_label in enumerate(line_labels):
    ax.scatter([], [], c='k', alpha=0.3, s=20, label=line_label)

ax.legend(title=data_labels[2], loc="upper left")
ax.grid(True)
ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel(data_labels[1], fontsize=12)

# create colorbar
cbar = plt.colorbar(ScalarMappable(norm=norm, cmap='viridis'))
cbar.set_label(data_labels[3])

plt.title("Overview of Departmental Performance in Employee Management")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/210_202312310045.png")
plt.clf()
