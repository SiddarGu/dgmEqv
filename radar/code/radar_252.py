import numpy as np
import matplotlib.pyplot as plt

# raw_data string
raw_data = "Athlete,Performance Q1,Performance Q2,Performance Q3,Performance Q4/n Athlete A,85,88,82,86/n Athlete B,80,82,85,81/n Athlete C,75,76,78,80/n Athlete D,70,74,76,78/n Athlete E,65,68,70,72"

# process the data string
raw_data = raw_data.replace("/n ", "\n").split("\n")
data_labels = raw_data[0].split(",")[1:]  # column labels
line_labels = [row.split(",")[0] for row in raw_data[1:]]  # row labels
data = np.array([list(map(int, row.split(",")[1:])) for row in raw_data[1:]])  # numerical data

# Create figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Compute angle each axis
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row
colors = plt.cm.viridis(np.linspace(0, 1, len(data)))

for i, row in enumerate(data):
    row = np.append(row, row[0])  # Append first element to end
    ax.plot(angles, row, color=colors[i], label=line_labels[i])  # Plot data line
    radius = np.full_like(angles, (i+1) * data.max() / len(data))  # Radius vector
    ax.plot(angles, radius, color=colors[i], linestyle='dotted')  # Gridlines

# Plot axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, rotation=45)

# Adjust radial limits
ax.set_ylim(0, data.max() * 1.1)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=90)

# Legend plot
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Remove circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Title
ax.set_title("Sports Performance Evaluation", size=20, color="black", pad=20)

# Adjust plot and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/104_2023122292141.png')

# Clear the current figure
plt.clf()
