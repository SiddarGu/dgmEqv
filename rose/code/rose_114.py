

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Renewable Energy', 'Waste Management', 'Air Quality', 'Water Quality', 'Sustainable Agriculture', 'Climate Change', 'Ecosystem Protection', 'Biodiversity Conservation']
data = [50, 35, 40, 70, 25, 90, 60, 45]
line_labels = ['Category','Number']

# Plot the data with the type of rose chart
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection='polar')

# Create sectors corresponding to different categories and assign different colors to each sector
sector_angle = (2*np.pi)/len(data_labels)
colors = ['#A9A9A9','#FF0000','#00FF00','#0000FF','#FFFF00','#FF00FF','#00FFFF','#000000']
for i in range(len(data_labels)):
    ax.bar(i*sector_angle, data[i], width=sector_angle, edgecolor='k', color=colors[i])

# Add legend next to the chart
ax.legend(data_labels, bbox_to_anchor=(1.08, 0.8))

# Set the ticks for the categories
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))

# Set the labels of the categories
ax.set_xticklabels(data_labels, fontsize=8, wrap=True)

# Set the title of the figure
ax.set_title('Environmental and Sustainability Initiatives and Their Levels of Success')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_106.png')

# Clear the current image state
plt.clf()