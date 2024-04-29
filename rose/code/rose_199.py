

import matplotlib.pyplot as plt
import numpy as np

# Transform data into three variables
data_labels = ['Renewable Energy', 'Carbon Footprint', 'Pollution', 'Climate Change', 'Biodiversity', 'Recycling', 'Water Resources', 'Waste Management']
data = [50, 45, 34, 30, 25, 20, 15, 10]
line_labels = ['Category', 'Number']

# Create figure and set polar coordinates
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1, 1, 1, projection='polar')

# Plot data with type of rose chart
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
angles = np.arange(0, 2 * np.pi, sector_angle)
ax.bar(angles, data, width=sector_angle, align='edge', alpha=0.5,
       edgecolor='black', color=['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF', '#C0C0C0', '#800080'])

# Set category labels and legend
ax.set_xticks(angles)
ax.set_xticklabels(data_labels, fontsize=15)
ax.legend(data_labels, fontsize=15, bbox_to_anchor=(1.1, 1.1))

# Set the title of the figure
ax.set_title('Impact of Environmental Issues on Sustainability Efforts', fontsize=20)

# Adjust the position of the legend so that it does not cover any part of the chart
ax.legend(bbox_to_anchor=(1.2, 1.1))

# Resize the image
plt.tight_layout()

# Save image
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_43.png")

# Clear the current image state
plt.clf()