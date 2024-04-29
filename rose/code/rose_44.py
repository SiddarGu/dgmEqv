

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Visual Arts', 'Music', 'Theatre', 'Literature', 'Film', 'Dance', 'Architecture', 'Photography']
data = [400, 200, 150, 100, 80, 60, 40, 20]
line_labels = ['Arts Category', 'Number of Artists']

# Create figure before plotting
fig = plt.figure(figsize=(10, 10))

# Plot the data with the type of rose chart
ax = fig.add_subplot(1, 1, 1, projection='polar', polar=True)

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot the sectors and assign labels
for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i])

# Add legend
ax.legend(bbox_to_anchor=(1.1, 1.1))

# Set xticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, wrap=True)

# Set title
ax.set_title('Number of Artists in Different Arts Fields in 2021', fontsize=20)

# Auto resize the image
plt.tight_layout()

# Save image
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_132.png')

# Clear the current image state
plt.clf()