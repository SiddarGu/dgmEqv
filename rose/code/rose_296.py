
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ['Biotechnology', 'Aerospace Engineering', 'Mechanical Engineering', 'Civil Engineering', 'Electrical Engineering', 'Chemical Engineering', 'Computer Science', 'Robotics']
data = [47, 96, 17, 36, 96, 60, 68, 50]
line_labels = ['Category', 'Number']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, polar=True)

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Create sectors corresponding to different categories
for i, data_val in enumerate(data):
    ax.bar(i * sector_angle, data_val, width=sector_angle, bottom=0.0, color=plt.cm.Set1(i / float(num_categories)), label=data_labels[i])

# Set the legend
ax.legend(bbox_to_anchor=(0.95, 0.1), fontsize='small', labels=data_labels)

# Set angle parameters for each sector
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize='small', wrap=True, rotation=-45)

# Set the title of the figure
plt.title('Number of Science and Engineering Projects in 2021')

# Resize the image to prevent content from being displayed
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-082906_5.png')

# Clear the current image state
plt.clf()