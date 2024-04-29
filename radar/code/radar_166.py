import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Q1","Q2","Q3","Q4"]
line_labels = ["Fossil Fuels (%)","Renewable Energy (%)","Energy Efficiency (%)","Power Generation (%)","Transmission & Distribution (%)"]
data = np.array([[50,55,60,65],[70,75,80,85],[65,70,75,80],[60,65,70,75],[80,85,90,95]])

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

ax.plot(angles, data[0], '-o', color='orange', label=line_labels[0])
ax.plot(angles, data[1], '-o', color='green', label=line_labels[1])
ax.plot(angles, data[2], '-o', color='blue', label=line_labels[2])
ax.plot(angles, data[3], '-o', color='red', label=line_labels[3])
ax.plot(angles, data[4], '-o', color='violet', label=line_labels[4])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)
ax.set_rlim(0,np.max(data))

max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=(0.9, 0.95))
ax.set_title("Energy and Utilities Performance - 2023", fontsize=15, pad=20)

ax.grid(True)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/31_202312262320.png")
plt.clf()