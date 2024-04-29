import matplotlib.pyplot as plt
import numpy as np

# Data preparation
given_data = "Category,Charity A,Charity B,Charity C,Charity D,Charity E/n Donation Received,80,85,90,95,100/n Project Impacts,70,75,80,85,90/n Volunteer Participation,95,90,85,80,75/n Operating Expenses,50,55,60,65,70/n Public Awareness,65,70,75,80,85"
given_data = given_data.replace("/n ", "\n").split("\n")
data_labels = given_data[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in given_data[1:]]
data = [list(map(int, line.split(",")[1:])) for line in given_data[1:]]

# Preparing angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Creating figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Plotting data
for i, row in enumerate(data):
    row.append(row[0])  # creating a closed loop
    ax.plot(angles, row, label=line_labels[i])
    radius = np.full_like(angles, ((i + 1) * max([max(sublist) for sublist in data]) / len(data)))
    ax.plot(angles, radius, color='grey', linestyle='--')

# Setting the gridlines
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, rotation=90)

# Adjusting the radial limits
ax.set_rlim(0, max([max(sublist) for sublist in data]))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plotting the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Adjusting aesthetics
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
ax.set_title('Charity and Nonprofit Organizations Performance Evaluation')

# Saving figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/108_2023122292141.png')

# Clearing figure
plt.clf()
