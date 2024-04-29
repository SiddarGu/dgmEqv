
import matplotlib.pyplot as plt
import numpy as np

# Transform data into three variables
data_labels = ['Web Development', 'Mobile Development', 'Networking', 'Data Science', 'Cyber Security', 'Cloud Computing', 'Artificial Intelligence', 'Big Data']
data = [86, 73, 58, 48, 34, 24, 14, 9]
line_labels = ['Category', 'Number']

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection='polar')

# Set up polar coordinates
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

# Create sectors
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot different categories in different colors
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i))

# Ensure angles of sectors add up to 360 degrees
ax.set_ylim(0, max(data) + 5)
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))

# Set labels for each sector
ax.set_xticklabels(data_labels, wrap=True, fontsize=14)

# Position the legend
ax.legend(loc=(0.75, 0.6), bbox_to_anchor=(1.15, 0.6))

# Set title
ax.set_title('Number of Technology and Internet Specialists in 2021', fontsize=20)

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_141.png')

# Clear current image state
plt.clf()