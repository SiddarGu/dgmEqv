import matplotlib.pyplot as plt
import numpy as np

data_str = """
Condition,Healthcare Facility A,Healthcare Facility B,Healthcare Facility C,Healthcare Facility D
Diabetes Control,80,75,85,70
Cancer Treatment,85,90,80,75
Cardiovascular Health,75,80,70,85
Infection Prevention,90,85,80,95
Mental Health Services,70,75,65,80
"""

data_lines = data_str.strip().split("\n")
data_labels = data_lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in data_lines[1:]]
data = np.array([list(map(int, line.split(",")[1:])) for line in data_lines[1:]])

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

for i, d in enumerate(data):
    d = np.append(d, d[0])  # close loop
    grid_values = np.full_like(angles, (i+1) * data.max() / len(data))
    ax.plot(angles, d, label=line_labels[i])
    ax.fill(angles, d, alpha=0.25)
    ax.plot(angles, grid_values, color="gray", linestyle="dotted")

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, rotation=45)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
ax.set_title("Comparison of Healthcare Services Across Facilities")
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")
    
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/151_2023122292141.png', dpi=300)
plt.clf()
