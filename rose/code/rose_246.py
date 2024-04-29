
import matplotlib.pyplot as plt
import numpy as np

# Transform data to three variables
data_labels = ['Physics', 'Chemistry', 'Mathematics', 'Computer Science', 'Electrical Engineering', 'Mechanical Engineering', 'Civil Engineering', 'Aerospace Engineering']
data = [125, 95, 50, 140, 120, 80, 60, 30]
line_labels = ['Category', 'Number of Programs']

# Get the number of categories
num_categories = len(data_labels)

# Calculate the sector angle
sector_angle = (2 * np.pi) / num_categories

# Create figure and axes
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

# Plot the chart
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], alpha=0.5)

# Set the tick labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, rotation=90, va='top', ha='center')

# Add legend and title
ax.legend(bbox_to_anchor=(1.1, 1.05))
ax.set_title('Number of Undergraduate Programs Offered in Science and Engineering Fields', fontsize=15)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_98.png')
plt.clf()