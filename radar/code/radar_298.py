import numpy as np
import matplotlib.pyplot as plt

# Define the data
raw_data = """Aspect, Hospital A, Hospital B, Hospital C, Hospital D
 Outpatient Satisfaction (%),88,86,84,82
 Inpatient Satisfaction (%),78,76,74,72
 Treatment Success Rate (%),92,90,88,86
 Staff Responsiveness (Score),7,8,9,10
 Operational Efficiency (Score),9,8,7,6 """

# Transform raw data into proper format
lines = raw_data.split("\n")
data_labels = lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in lines[1:]]
data = np.array([[int(num) for num in line.split(",")[1:]] for line in lines[1:]])

# Create radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i, row in enumerate(data):
    row = np.append(row, row[0])  # Close the loop
    ax.plot(angles, row, label=line_labels[i])
    gridline_radii = np.full_like(angles, (i + 1) * max(data.ravel()) / len(data))
    ax.plot(angles, gridline_radii, color='lightgray', linestyle='--')

# Remove circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Plot axis labels
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)

# Set radial limits
ax.set_rlim(0, max(data.ravel()) * 1.1)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=90)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", title="Hospitals")

ax.set_title("Comparative Analysis of Healthcare Institutions", size=20, color='black', y=1.1)
# Adjust labels, title and save figure
plt.tight_layout()
fig.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/193_2023122292141.png")

plt.close(fig)
