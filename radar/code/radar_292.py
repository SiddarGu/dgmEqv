import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Prepare the data
data_string = "Field,19th Century,20th Century,Contemporary Art,Postmodern Art/n Art Appreciation,90,80,70,60/n Installation Art Interest,70,85,95,100/n Abstract Art Popularity,85,75,68,55/n Cubism Relevance,80,90,75,60/n Surrealism Recognition,75,85,92,70"
data_lines = data_string.split("/n ")

data_labels = data_lines[0].split(",")[1:]
data = np.array([list(map(int, line.split(",")[1:])) for line in data_lines[1:]])
line_labels = [line.split(",")[0] for line in data_lines[1:]]

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

colors = plt.cm.get_cmap('hsv', len(data)+1)

for i, row in enumerate(data):
    data_row = np.append(row, row[0])
    line, = ax.plot(angles, data_row, '-', color=colors(i), label=line_labels[i])

    radius = np.full_like(angles, (i + 1) * np.amax(data) / len(data))
    gridline, = ax.plot(angles, radius, '-', color=colors(i), alpha=0.5)

    line.set_label(line_labels[i])
    
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels, wrap=True)  # Set the axis label
ax.set_rlim(0, np.ceil(np.amax(data) / 10) * 10)  # Adjust the radial limits to accommodate the max of data
ax.yaxis.grid(False)  # Remove the circular gridlines
ax.spines['polar'].set_visible(False)  # Remove the background
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=-90)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc="upper right", bbox_to_anchor=(1.1, 1.1))  # Plot the legend of data lines

plt.title('Evolution of Art Styles Through Centuries', size=20, color='black', y=1.1)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/164_2023122292141.png')
plt.clf()  # Clear the current image state
