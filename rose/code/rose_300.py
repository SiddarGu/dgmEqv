
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ['Humanitarian Aid', 'Environmental Protection', 'Education', 'Healthcare', 'Poverty Alleviation', 'Animal Welfare', 'Arts and Culture', 'Disaster Relief', 'Social Services']
data = [150, 100, 140, 120, 90, 80, 60, 40, 20]
line_labels = ['Category', 'Number of Organizations']

# Create figure and adjust the axes to use polar coordinates
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)

# Calculate the sector angle and draw sectors corresponding to different categories
sector_angle = (2 * np.pi) / len(data_labels)
for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.tab20c(i))

# Add legend outside of the chart
ax.legend(bbox_to_anchor=(1.1, 1.1))

# Setting x-axis ticks and labels
ax.set_xticks(np.linspace(0, 2 * np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, rotation=30, fontsize=14)

# Setting title
ax.set_title('Number of Charitable and Nonprofit Organizations by Category', fontsize=16)

# Automatically resize the image with tight_layout
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/5.png')

# Clear the image state
plt.cla()