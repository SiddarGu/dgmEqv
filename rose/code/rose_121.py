

import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Renewable Energy','Energy Efficiency','Sustainable Agriculture','Carbon Emissions Reduction','Water Conservation','Waste Management','Air Pollution Reduction','Habitat and Wildlife Preservation','Climate Change Mitigation']
data = [90,87,65,50,45,40,35,30,25]
line_labels = ['Category','Number']

# Create a figure
fig = plt.figure(figsize=(16,8))

# Create a subplot
ax = fig.add_subplot(111, projection='polar')

# Calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Generate sectors
for i in range(num_categories):
    ax.bar(x=i * sector_angle, width=sector_angle, bottom=0.0, height=data[i], label=data_labels[i], color=plt.cm.Set1(i % 9))

# Set ticks and labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, wrap=True, rotation=45)

# Add title
ax.set_title('Number of Global Initiatives Related to Sustainability in 2020')

# Add legend
ax.legend(data_labels, bbox_to_anchor=(1.15, 1.05))

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_120.png')

# Clear the current image state
plt.clf()