
import matplotlib.pyplot as plt
import numpy as np

# Transform the data into variables
data_labels = ['Search Engines', 'Social Networking', 'Video Streaming', 'News Outlets', 'Blogging Platforms', 'Online Shopping', 'Online Forums']
data = [200, 150, 100, 80, 60, 40, 20]
line_labels = ['Social Media Category', 'Number']

# Plot the data
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1,1,1, projection='polar')

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Set up the different colors
colors = ['lightcoral', 'gold', 'royalblue', 'plum', 'darkseagreen', 'cadetblue', 'magenta']

# Plot the sectors
for i, category in enumerate(data_labels):
    ax.bar(i * sector_angle, data[i], width=sector_angle, color=colors[i], label=category)

# Set up the legend
ax.legend(data_labels, bbox_to_anchor=(1.2, 1.1))

# Set up the x-axis ticks
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, wrap=True)

# Set up the title
ax.set_title('Popularity of Social Media Platforms in 2021')

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_18.png')

# Clear the current image state
plt.clf()