
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Strength (MPa)', 'Flexibility (%)', 'Weight (kg/m3)', 'Corrosion Resistance (Score)', 'Cost (USD/kg)']
line_labels = ['Steel', 'Aluminium', 'Copper', 'Plastic', 'Concrete']
data = np.array([[500, 300, 785, 700, 800],
                 [280, 500, 270, 500, 200],
                 [220, 700, 896, 800, 600],
                 [100, 200, 120, 600, 150],
                 [70, 100, 240, 900, 500]])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for row in range(len(data)):
    ax.plot(angles, data[row], marker='o', label=line_labels[row])

ax.xaxis.set_major_locator(plt.MaxNLocator(len(data_labels)))
ax.set_xticklabels(data_labels)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=12, rotation=0, wrap=True)
ax.set_rlim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc=(1.1, 0.9), title="Materials")

plt.title("Comparison of Engineering Materials Properties")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/53_202312302350.png")

plt.clf()