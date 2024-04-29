

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Wellness', 'Cardiovascular', 'Mental Health', "Women's Health", 'Oral Health', 'Nutrition', 'Immunology', 'Endocrinology']
data = [50, 42, 36, 30, 24, 18, 12, 6]
line_labels = ['Health Category', 'Number']

# Plot the data with the type of rose chart.
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1, projection='polar')

# Create different sectors in the graph.
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot the data with a loop.
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i])

# Create a legend and adjust the position.
ax.legend(bbox_to_anchor=(1.2, 0.5))

# Set the number of ticks and the corresponding labels.
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=14)

# Make sure the legend does not overlap with the chart.
plt.tight_layout()

# Set the title of the figure.
plt.title('Number of Patients Visiting Healthcare Providers for Each Health Category', fontsize=16)

# Save the image.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_113.png')

# Clear the current figure.
plt.clf()