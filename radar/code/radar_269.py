import matplotlib.pyplot as plt
import numpy as np

# Split and transform the given string into structured dataset
raw = "Factors,Q1,Q2,Q3,Q4/n Employee Satisfaction,85,90,95,100/n Training Effectiveness,70,75,80,85/n Performance Rating,80,85,90,95/n Teamwork Quality,75,80,85,90/n Turnover Rate,55,50,45,40"
lines = raw.split("/n ")
lines = [line.split(",") for line in lines]
data_labels = lines[0][1:]
line_labels = [line[0] for line in lines[1:]]
data = np.array([list(map(int, line[1:])) for line in lines[1:]])

# Create a figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(projection='polar')

# Define the angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels, rotation=45)

# Plot each row in the data
colors = ['blue', 'orange', 'green', 'red', 'purple']

for i, row in enumerate(data):
    row = np.append(row, row[0])  # create a 'closed loop'
    ax.plot(angles, row, color = colors[i], label=line_labels[i])
    ax.fill(angles, row, color = colors[i], alpha=0.25)
    ax.plot(angles, np.full_like(angles, (i+1) * np.max(data) / len(data), dtype=float), color='grey', linestyle='dashed')

# Aesthetics
ax.spines['polar'].set_visible(False)
ax.set_rlim(bottom=0, top=np.max(data))
ax.set_title("Human Resources and Employee Management Assessment")
ax.yaxis.grid(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Save and clear the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/97_2023122292141.png')
plt.clf()
