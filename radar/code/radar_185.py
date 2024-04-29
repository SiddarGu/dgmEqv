import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_string = 'Sector,Q1,Q2,Q3,Q4\n Manufacturing,80,85,90,95\n Information Technology,70,75,80,85\n Real Estate,60,65,70,75\n Financial Services,90,95,100,105\n Retail Trade,80,85,90,95'
data_lines = data_string.split("\n")
data_labels = data_lines[0].split(",")[1:]
data = [list(map(int, x.split(",")[1:])) for x in data_lines[1:]]
line_labels = [x.split(",")[0] for x in data_lines[1:]]

data = np.array(data)
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for idx, d in enumerate(data):
    d = np.concatenate((d, [d[0]]))  # closing the polygonal line
    ax.fill(angles, d, alpha=0.25)
    ax.plot(angles, d, label=line_labels[idx])
    radius = np.full_like(angles, ((idx+1) * np.max(data)) / len(data))
    ax.plot(angles, radius, color='black', linestyle='--', linewidth=0.5)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_rlim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.set_title("Sector Performance Analysis - 2024")
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/124_2023122292141.png")
plt.close(fig)
