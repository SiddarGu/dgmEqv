import matplotlib.pyplot as plt
import numpy as np


data = """
Category,Truck,Ship,Airplane,Train
Delivery Time (Days),2,5,1,3
Fuel Efficiency (km/l),15,10,8,18
Capacity (Tons),20,24,12,20
Cost per Trip ($),50,20,15,30
Safety Rating (Score),85,75,90,95
"""

lines = data.split("\n")[1:-1]
data_labels = lines[0].split(",")[1:]
data = [list(map(float, line.split(",")[1:])) for line in lines[1:]]
line_labels = [line.split(",")[0] for line in lines[1:]]

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)

for idx, d in enumerate(data):
    d.append(d[0])
    ax.plot(angles, d, label=line_labels[idx])
    ax.fill(angles, np.full_like(angles, (idx+1) * max(max(data)) / len(data)), color='lightgray', alpha=0.1)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_rlim(0, max(max(data)))
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, data_labels, loc="upper right")
plt.title("Logistics Vehicle Performance Comparison")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/174_2023122292141.png")
plt.close()
