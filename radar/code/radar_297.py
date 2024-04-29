import matplotlib.pyplot as plt
import numpy as np

# raw data
raw_data_str = "Policy Area,Q1,Q2,Q3,Q4/n Education,85,88,91,94/n Healthcare,73,77,81,85/n Public Safety,79,82,85,88/n Environment,81,84,87,90/n \
Economic Development,88,92,96,100"

# parsing data
raw_data_list = raw_data_str.split("/n ")
rows = [r.split(",") for r in raw_data_list]
data_labels = rows[0][1:]
line_labels = [row[0] for row in rows[1:]]
data_num = [[float(value) for value in row[1:]] for row in rows[1:]]

# process numerical data
data = []
max_data = 0
min_data = 100
for row in data_num:
    max_data = max(max_data, max(row))
    min_data = min(min_data, min(row))
    row.append(row[0])
    data.append(np.array(row))

# creating radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# plot data and gridlines
for i in range(len(data)):
    color = plt.cm.viridis(i / len(data))
    ax.plot(angles, data[i], linewidth=2, label=line_labels[i])
    radius = np.full_like(angles, ((i+1) * max_data) / len(data))
    ax.plot(angles, radius, color='grey', linestyle='--')

# plot details
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(min_data - 10, max_data)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# aesthetics
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
plt.title("Government Policy Performance Index", size=20, color="black", pad=20)

# save and show
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/94_2023122292141.png')
plt.clf()
