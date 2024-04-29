
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ['Full Time', 'Part Time', 'Contractual', 'Remote', 'Interns', 'Freelancers']
data = [200, 100, 60, 50, 30, 20]
line_labels = ['Employee Type', 'Number']

# Create figure before plotting
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

# Set up the axes in polar coordinates
ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi/2)

# Set up the size of sectors
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot the data
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i],
           color=plt.cm.get_cmap('tab10').colors[i])

# Set ticks
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels)

# Position the legend
ax.legend(bbox_to_anchor=(1.05, 0.5), loc="center left")

# Add title
ax.set_title("Number of Employees by Type in 2021")

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_83.png')

# Clear the current image state
plt.clf()