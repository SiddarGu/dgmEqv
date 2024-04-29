
import matplotlib.pyplot as plt
import numpy as np

# Transform data into separate variables
data_labels = ['Math', 'Science', 'English', 'History', 'Computer Science', 'Physical Education', 'Art', 'Music']
data = [50, 45, 30, 40, 25, 20, 15, 10]
line_labels = ['Category', 'Number']

# Plot the data in a rose chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

# Set up the axes in polar coordinates
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

# Set the number of ticks to match the number of data points
num_categories = len(data_labels)
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))

# Calculate the width of each sector
sector_angle = (2 * np.pi) / num_categories

# Plot each sector with a different color
for i, data_val in enumerate(data):
    ax.bar(i * sector_angle, data_val, width=sector_angle, label=data_labels[i], color='C' + str(i))

# Draw the legend outside the main chart area
ax.legend(bbox_to_anchor=(1.2, 1.0))

# Set the category labels to the center position of each sector
ax.set_xticklabels(data_labels, rotation=90, wrap=True)

# Set title and display the chart
ax.set_title('Number of Students Enrolled in Each Subject in 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_128.png')
plt.clf()