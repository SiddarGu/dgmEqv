import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize
from matplotlib.colorbar import ColorbarBase

data_labels = ['Number of Employees','Average Job Satisfaction (Score)','Average Monthly Salary ($)','Employee Turnover Rate (%)']
raw_data = [['HR',35,80,2400,15],['Sales',120,75,2300,20],['Marketing',70,82,3000,18],['R&D',60,85,3500,10],['IT',45,70,3300,16],['Finance',50,75,2800,12],['Operations',110,70,2500,20]]
data = np.array([i[1:] for i in raw_data])
line_labels = [f"{i[0]} {i[1]}" for i in raw_data]

cmap = get_cmap('viridis')
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
colors = cmap(norm(data[:, 3]))
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

fig, ax = plt.subplots(figsize=(16, 8))

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=bubble_sizes[i], c=colors[i], label=None, alpha=0.7)
    ax.scatter([],[],c=colors[i], label=line_labels[i])

ax.legend(title=data_labels[2], loc='upper left')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

cax = fig.add_axes([0.92, 0.1, 0.02, 0.8]) #left, bottom, width, height
ColorbarBase(cax, cmap='viridis', norm=norm).set_label(data_labels[3])

plt.title('Job Satisfaction and Employee Management across Various Departments',fontsize=16)
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/295_202312310045.png', bbox_inches='tight')
plt.clf()
