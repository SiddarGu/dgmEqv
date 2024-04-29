import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data = np.array([[80, 85, 90, 95, 100],
                 [70, 75, 80, 85, 90],
                 [75, 80, 85, 90, 95],
                 [65, 70, 75, 80, 85],
                 [90, 95, 80, 85, 90]])

data_labels = ["Donation Efficiency (%)",
               "Fundraising Efficiency (%)",
               "Program Expenses (%)",
               "Administrative Expenses (%)",
               "Operational Sustainability (%)"]

line_labels = ["Aspect",
               "Red Cross",
               "UNICEF",
               "World Vision",
               "Save the Children",
               "Doctors Without Borders"]

# Create figure
plt.figure(figsize=(8, 8))
ax = plt.subplot(1, 1, 1, polar=True)

# Evenly space the axes
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append the first numerical element of each row to close the loop
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot each data line with different colors
colors = ['red', 'blue', 'green', 'purple', 'orange']

for i, line in enumerate(data):
    ax.plot(angles, line, color=colors[i], linewidth=1, label=line_labels[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
legend = plt.legend(handles, line_labels, bbox_to_anchor=(1.2, 1), loc='upper right')

# Set title
plt.title("Charity and Nonprofit Organizations Performance Analysis")

# Add background grid
ax.yaxis.grid(True)

# Adjust layout
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/169_202312310100.png')

# Clear the current image state
plt.clf()