import matplotlib.pyplot as plt
import numpy as np

raw_data = """Aspect,Small Firms,Medium Firms,Large Firms,Corporate Firms
Case Victories,83,86,89,92
Client Satisfaction,80,85,90,95
Cost Efficiency,78,80,82,84
Staff Performance,75,80,85,90
Regulation Compliance,85,87,89,91"""

raw_data = [row.split(",") for row in raw_data.split("\n")]

data_labels = raw_data[0][1:]
line_labels = [row[0] for row in raw_data[1:]]
data = np.array([list(map(int, row[1:])) for row in raw_data[1:]])

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

for i, row_data in enumerate(data):
    row_data = np.append(row_data, row_data[0]) # append first element to end for close-loop
    ax.plot(angles, row_data, label=line_labels[i])

    gridline_locations = np.full_like(angles, (i+1) * data.max() / len(data))
    ax.plot(angles, gridline_locations, color='silver', linewidth=0.5) # gridlines

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True) # axis labels
ax.set_rlim([0, data.max() + 10]) # adjust radial limits
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.yaxis.grid(False) # remove y-axis gridlines
ax.spines['polar'].set_visible(False) # remove background

handles, labels = ax.get_legend_handles_labels() # legend
ax.legend(handles, line_labels, loc="upper right")

fig.suptitle("Performance Comparison of Law Firms") # title
fig.tight_layout() # automatic resize
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/114_2023122292141.png", dpi=300) # save figure
plt.clf() # clear
