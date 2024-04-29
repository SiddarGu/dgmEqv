import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data_labels = ["Treatment Success Rate (%)", "Doctor Retention Rate (%)", "Patient Admission Rate (%)", "Facility Upgrade Rate (%)", "Mortality Rate (%)"]
line_labels = ["General Hospital", "Women's Health Center", "Pediatric Hospital", "Psychiatric Hospital", "Orthopedic Hospital", "Geriatric Hospital"]
data = np.array([[90, 85, 80, 85, 73],
                 [88, 86, 76, 88, 72],
                 [92, 84, 79, 90, 81],
                 [89, 83, 78, 86, 84],
                 [91, 88, 82, 87, 83],
                 [87, 84, 74, 89, 82]])

# Create figure
fig = plt.figure(figsize=(10, 8))

# Add subplot
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append first element of each row to close the loop
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot data lines with different colors
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], linewidth=2, label=line_labels[i])

# Set axis labels and radial limits
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc="upper right")

# Set title
plt.title("Health and Healthcare Quality Indicators Analysis")

# Adjust layout and save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/63_202312302350.png')

# Clear current image state
plt.clf()