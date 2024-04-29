
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Pollution', 'Renewable Energy', 'Carbon Emissions', 'Waste Management', 'Eco-Friendliness']
line_labels = ['Region A', 'Region B', 'Region C', 'Region D']
data = np.array([[75, 80, 85, 90], [65, 70, 75, 80], [50, 55, 60, 65], [85, 90, 95, 100], [80, 85, 90, 95]])

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1, 1, 1, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i in range(len(line_labels)):
    data_line = np.append(data[:,i], data[0,i])
    ax.plot(angles, data_line, 'o-', linewidth=2, label=line_labels[i])
    ax.fill(angles, data_line, alpha=0.25)
    ax.plot(angles, np.full_like(angles, (i+1) * np.max(data)/len(line_labels)), '-', color='gray', alpha=0.2)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)
ax.set_ylim(0, np.max(data))
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
plt.title('Regional Sustainability Evaluation', fontsize=16)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/12.png')
plt.clf()