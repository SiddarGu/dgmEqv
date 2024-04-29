import matplotlib.pyplot as plt
import numpy as np

# original data
original_data = ["School Aspect,Primary School,High School,Undergraduate,Graduate",
                "Literacy Rate,85,90,95,99",
                "Student Attendance,90,88,92,95",
                "Faculty Qualification,70,80,85,90",
                "Infrastructure Quality,75,80,85,90",
                "Research Output,na,na,80,85"]

# extract data_labels, data, line_labels
data = []
line_labels = []
for row in original_data[1:]:
    split_row = row.split(",")
    line_labels.append(split_row[0])
    real_values = [float(value) if value != 'na' else 0.0 for value in split_row[1:]]
    data.append(real_values)
   
data_labels = original_data[0].split(",")[1:]

# create a radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)

# plot each line_data
colors = plt.cm.viridis(np.linspace(0, 1, len(data)))
for i, line_data in enumerate(data):
    line_data += line_data[:1]
    ax.plot(angles, line_data, color=colors[i], label=line_labels[i])
    ax.fill(angles, line_data, color=colors[i], alpha=0.25)
    radius = np.full_like(angles, (i+1) * max([item for sublist in data for item in sublist]) / len(data))
    ax.plot(angles, radius, color=colors[i], linestyle="dotted")

# adjust the radial limits and gridlines
ax.set_rlim(0, max([item for sublist in data for item in sublist]) + 10)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# add legend & title
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.1, 1.1))
plt.title("Education Efficiency Evaluation by School Level", size=20, color='black', y=1.1)

# save & show fig
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/76_2023122292141.png')
plt.clf()
