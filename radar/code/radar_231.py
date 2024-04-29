import numpy as np
import matplotlib.pyplot as plt

# data
data_lines = ["Element,Power Station A,Power Station B,Power Station C,Power Station D",
              "Energy Production,90,85,80,75",
              "Resource Efficiency,80,75,70,65",
              "Waste Management,70,75,80,85",
              "Safety Measures,85,90,95,100",
              "Sustainability Practices,75,70,75,80"]

data = [list(map(int, line.split(',')[1:])) for line in data_lines[1:]]
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]

# calculation for plot
num_vars = len(data_labels)
max_val = np.max(np.array(data))
angles = np.linspace(0, 2 * np.pi, num_vars + 1, endpoint=True)

# create figure
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# iterate over each row
for i, d in enumerate(data):
    d.append(d[0])  # append the start value to end to close loop
    ax.plot(angles, d, linewidth=0.6, label=line_labels[i])    # plot data
    ax.fill(angles, d, alpha=0.25)       # fill area
    ax.plot(angles, np.full_like(angles, (i+1) * max_val / len(data)), color='black', linewidth=0.25)  # plot gridlines

# labels and legend
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)   # set axis label
ax.set_rlabel_position(30)   # move radial labels away from plotted line
ax.set_rlim(bottom=0, top=max_val)  # adjust radial limits
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=-90)

plt.title('Energy and Utility Stations Performance Analysis', size=20, color='black', y=1.1)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# aesthetics improvement
ax.spines['polar'].set_visible(False)   # hide the polar background
ax.xaxis.grid(True, color='black', linestyle='solid', linewidth=0.5)   # draw xaxis grid
ax.yaxis.grid(False)   # hide the yaxis grid

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/115_2023122292141.png', format='png')
plt.clf()
