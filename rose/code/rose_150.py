

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Technology', 'Electrical Engineering', 'Computer Engineering', 'Civil Engineering', 'Mechanical Engineering', 'Manufacturing Engineering', 'Aerospace Engineering', 'Biomedical Engineering', 'Chemistry']
data = [85, 75, 87, 95, 90, 85, 80, 70, 60]
line_labels = ['Discipline', 'Number of Institutions']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(111, polar=True)

# Create sectors corresponding to different categories, assign a different color to each sector
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#FFFF00', '#FFA500']
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

# Set the title
ax.set_title('Number of Academic Institutions in Different Fields of Science and Engineering', fontsize=18)

# Set the angles of tick labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=14, ha='center')

# Set the legend
ax.legend(data_labels, fontsize=14, bbox_to_anchor=(1.3,1), loc="upper right")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_36.png')

# Clear the current image state
plt.close()