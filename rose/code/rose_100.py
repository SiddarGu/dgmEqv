

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Education', 'Health', 'Social Welfare', 'Human Rights', 'Environment', 'Arts and Culture', 'Religion', 'Animal Welfare', 'International Development']
data = [50, 75, 60, 35, 45, 30, 20, 15, 10]
line_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

# Modify the axes to use polar coordinates
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_rlabel_position(0)

# Calculate the sector angle
sector_angle = (2 * np.pi) / len(data_labels)

# Plot the data
for i in range(len(data_labels)):
    ax.bar(sector_angle*i, data[i], width=sector_angle, bottom=0.0, label=data_labels[i], color=np.random.rand(3,))

# Set the axes ticks
ax.set_xticks(sector_angle*np.arange(len(data_labels)))
ax.set_xticklabels(data_labels, fontsize=12)

# Reposition the legend
ax.legend(bbox_to_anchor=(1.2, 1.0))

# Set the title
ax.set_title("Number of Nonprofits by Type in 2021", fontsize=18)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_92.png')

# Clear the current image state
plt.clf()